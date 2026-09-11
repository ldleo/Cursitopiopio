package com.ldleo.isolatedbrowser

import android.app.Dialog
import android.graphics.Bitmap
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Bundle
import android.view.View
import android.view.ViewGroup
import android.view.Window
import android.webkit.*
import android.widget.*
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity
import androidx.webkit.ProfileStore
import androidx.webkit.WebViewCompat
import androidx.webkit.WebViewFeature
import org.json.JSONArray
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL

class MainActivity : AppCompatActivity() {

    private val profiles = mutableListOf<BrowserProfile>()
    private var activeProfile: BrowserProfile? = null

    private lateinit var tvVpnStatus: TextView
    private lateinit var btnRefreshIp: TextView
    private lateinit var btnProfilesList: Button
    private lateinit var btnCreateProfileTop: Button
    private lateinit var profilesScreen: LinearLayout
    private lateinit var tvEmptyMessage: TextView
    private lateinit var scrollProfiles: ScrollView
    private lateinit var llProfilesContainer: LinearLayout
    private lateinit var btnNewProfileBig: Button

    private lateinit var browserScreen: LinearLayout
    private lateinit var tvActiveBadge: TextView
    private lateinit var btnClearCurrentSession: Button
    private lateinit var webViewContainer: FrameLayout
    private var activeWebView: WebView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initViews()
        loadProfilesFromPrefs()
        refreshProfilesUi()
        fetchVpnStatus()

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (browserScreen.visibility == View.VISIBLE) {
                    if (activeWebView?.canGoBack() == true) {
                        activeWebView?.goBack()
                    } else {
                        showProfilesScreen()
                    }
                } else {
                    finish()
                }
            }
        })
    }

    private fun initViews() {
        tvVpnStatus = findViewById(R.id.tvVpnStatus)
        btnRefreshIp = findViewById(R.id.btnRefreshIp)
        btnProfilesList = findViewById(R.id.btnProfilesList)
        btnCreateProfileTop = findViewById(R.id.btnCreateProfileTop)

        profilesScreen = findViewById(R.id.profilesScreen)
        tvEmptyMessage = findViewById(R.id.tvEmptyMessage)
        scrollProfiles = findViewById(R.id.scrollProfiles)
        llProfilesContainer = findViewById(R.id.llProfilesContainer)
        btnNewProfileBig = findViewById(R.id.btnNewProfileBig)

        browserScreen = findViewById(R.id.browserScreen)
        tvActiveBadge = findViewById(R.id.tvActiveBadge)
        btnClearCurrentSession = findViewById(R.id.btnClearCurrentSession)
        webViewContainer = findViewById(R.id.webViewContainer)

        btnRefreshIp.setOnClickListener { fetchVpnStatus() }
        btnCreateProfileTop.setOnClickListener { showNewProfileDialog() }
        btnNewProfileBig.setOnClickListener { showNewProfileDialog() }
        btnProfilesList.setOnClickListener { showProfilesScreen() }
        btnClearCurrentSession.setOnClickListener { clearCurrentSessionAndExit() }
    }

    private fun fetchVpnStatus() {
        tvVpnStatus.text = "🌐 Consultando red / VPN..."
        Thread {
            try {
                val url = URL("http://ip-api.com/json")
                val conn = url.openConnection() as HttpURLConnection
                conn.connectTimeout = 4000
                conn.readTimeout = 4000
                val reader = BufferedReader(InputStreamReader(conn.inputStream))
                val response = reader.readText()
                reader.close()

                val json = JSONObject(response)
                val ip = json.optString("query", "Desconocida")
                val country = json.optString("country", "Desconocido")
                val code = json.optString("countryCode", "")

                runOnUiThread {
                    tvVpnStatus.text = "🌐 IP: $ip | País: $country ($code) 🟢"
                }
            } catch (e: Exception) {
                runOnUiThread {
                    tvVpnStatus.text = "🌐 Red activa (No se pudo geolocalizar IP)"
                }
            }
        }.start()
    }

    private fun showNewProfileDialog() {
        val dialog = Dialog(this)
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE)
        dialog.setContentView(R.layout.dialog_new_profile)
        dialog.window?.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
        dialog.window?.setLayout(
            (resources.displayMetrics.widthPixels * 0.90).toInt(),
            ViewGroup.LayoutParams.WRAP_CONTENT
        )

        val etName = dialog.findViewById<EditText>(R.id.etProfileName)
        val etUrl = dialog.findViewById<EditText>(R.id.etProfileUrl)
        val tvError = dialog.findViewById<TextView>(R.id.tvUrlError)
        val btnSave = dialog.findViewById<Button>(R.id.btnSaveOnly)
        val btnSaveAndOpen = dialog.findViewById<Button>(R.id.btnSaveAndOpen)
        val btnCancel = dialog.findViewById<TextView>(R.id.btnCancelDialog)

        fun validateAndCreate(openImmediately: Boolean) {
            val name = etName.text.toString().trim().ifEmpty { "Perfil ${profiles.size + 1}" }
            val rawUrl = etUrl.text.toString().trim()

            if (!rawUrl.startsWith("http://") && !rawUrl.startsWith("https://")) {
                tvError.visibility = View.VISIBLE
                return
            }
            tvError.visibility = View.GONE

            val newId = "profile_${System.currentTimeMillis()}"
            val seed = (1000..99999).random()
            val gpuIndex = profiles.size % BrowserProfile.GPU_LIST.size
            val gpu = BrowserProfile.GPU_LIST[gpuIndex]

            val newProfile = BrowserProfile(
                id = newId,
                name = name,
                startUrl = rawUrl,
                seed = seed,
                gpuVendor = gpu.first,
                gpuRenderer = gpu.second
            )

            profiles.add(newProfile)
            saveProfilesToPrefs()
            refreshProfilesUi()
            dialog.dismiss()

            if (openImmediately) {
                launchProfile(newProfile)
            }
        }

        btnSave.setOnClickListener { validateAndCreate(false) }
        btnSaveAndOpen.setOnClickListener { validateAndCreate(true) }
        btnCancel.setOnClickListener { dialog.dismiss() }

        dialog.show()
    }

    private fun launchProfile(profile: BrowserProfile) {
        activeProfile = profile
        tvActiveBadge.text = "● ${profile.name} [${profile.gpuRenderer}]"

        activeWebView?.let {
            it.onPause()
            it.pauseTimers()
            webViewContainer.removeView(it)
            it.destroy()
        }

        val webView = WebView(this)
        webView.layoutParams = ViewGroup.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT
        )

        val settings = webView.settings
        settings.javaScriptEnabled = true
        settings.domStorageEnabled = true
        settings.databaseEnabled = true
        settings.cacheMode = WebSettings.LOAD_DEFAULT
        settings.mediaPlaybackRequiresUserGesture = true

        if (WebViewFeature.isFeatureSupported(WebViewFeature.MULTI_PROFILE)) {
            val profileStore = ProfileStore.getInstance()
            val webkitProfile = profileStore.getOrCreateProfile(profile.id)
            webkitProfile.cookieManager.setAcceptCookie(true)
            WebViewCompat.setProfile(webView, webkitProfile.name)
        }

        webView.webViewClient = object : WebViewClient() {
            override fun onPageStarted(view: WebView?, url: String?, favicon: Bitmap?) {
                super.onPageStarted(view, url, favicon)
                val script = StealthScript.generate(profile.seed, profile.gpuVendor, profile.gpuRenderer)
                view?.evaluateJavascript(script, null)
            }

            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
                val targetUrl = request?.url?.toString() ?: return false
                view?.loadUrl(targetUrl)
                return true
            }
        }

        webView.webChromeClient = object : WebChromeClient() {
            override fun onPermissionRequest(request: PermissionRequest?) {
                request?.deny()
            }
        }

        activeWebView = webView
        webViewContainer.addView(webView)

        profilesScreen.visibility = View.GONE
        browserScreen.visibility = View.VISIBLE

        webView.loadUrl(profile.startUrl)
    }

    private fun showProfilesScreen() {
        activeWebView?.let {
            it.onPause()
            it.pauseTimers()
        }
        browserScreen.visibility = View.GONE
        profilesScreen.visibility = View.VISIBLE
        refreshProfilesUi()
    }

    private fun clearCurrentSessionAndExit() {
        activeProfile?.let { profile ->
            if (WebViewFeature.isFeatureSupported(WebViewFeature.MULTI_PROFILE)) {
                val profileStore = ProfileStore.getInstance()
                val webkitProfile = profileStore.getProfile(profile.id)
                webkitProfile?.cookieManager?.removeAllCookies(null)
                webkitProfile?.webStorage?.deleteAllData()
            }
            activeWebView?.clearCache(true)
            activeWebView?.clearHistory()
            Toast.makeText(this, "Sesión borrada por completo", Toast.LENGTH_SHORT).show()
        }
        showProfilesScreen()
    }

    private fun refreshProfilesUi() {
        llProfilesContainer.removeAllViews()

        if (profiles.isEmpty()) {
            tvEmptyMessage.visibility = View.VISIBLE
            scrollProfiles.visibility = View.GONE
        } else {
            tvEmptyMessage.visibility = View.GONE
            scrollProfiles.visibility = View.VISIBLE

            for (profile in profiles) {
                val card = LinearLayout(this)
                card.orientation = LinearLayout.VERTICAL
                card.setBackgroundResource(R.drawable.bg_card)
                val params = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                )
                params.setMargins(0, 0, 0, 16)
                card.layoutParams = params
                card.setPadding(24, 24, 24, 24)

                val tvName = TextView(this)
                tvName.text = profile.name
                tvName.textSize = 16f
                tvName.setTextColor(Color.WHITE)
                card.addView(tvName)

                val tvUrl = TextView(this)
                tvUrl.text = profile.startUrl
                tvUrl.textSize = 12f
                tvUrl.setTextColor(Color.parseColor("#8E8E93"))
                tvUrl.setPadding(0, 4, 0, 8)
                card.addView(tvUrl)

                val tvHardware = TextView(this)
                tvHardware.text = "GPU: ${profile.gpuRenderer} | Seed: #${profile.seed}"
                tvHardware.textSize = 11f
                tvHardware.setTextColor(Color.parseColor("#34C759"))
                card.addView(tvHardware)

                val buttonsRow = LinearLayout(this)
                buttonsRow.orientation = LinearLayout.HORIZONTAL
                buttonsRow.setPadding(0, 12, 0, 0)

                val btnOpen = Button(this)
                btnOpen.text = "Abrir"
                btnOpen.setBackgroundColor(Color.parseColor("#C5B3F9"))
                btnOpen.setTextColor(Color.BLACK)
                btnOpen.setOnClickListener { launchProfile(profile) }
                buttonsRow.addView(btnOpen)

                val btnDelete = Button(this)
                btnDelete.text = "Eliminar"
                btnDelete.setBackgroundColor(Color.parseColor("#FF453A"))
                btnDelete.setTextColor(Color.WHITE)
                val deleteParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.WRAP_CONTENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                )
                deleteParams.setMargins(16, 0, 0, 0)
                btnDelete.layoutParams = deleteParams
                btnDelete.setOnClickListener {
                    profiles.remove(profile)
                    saveProfilesToPrefs()
                    refreshProfilesUi()
                }
                buttonsRow.addView(btnDelete)

                card.addView(buttonsRow)
                llProfilesContainer.addView(card)
            }
        }
    }

    private fun saveProfilesToPrefs() {
        val prefs = getSharedPreferences("browser_profiles", MODE_PRIVATE)
        val array = JSONArray()
        for (p in profiles) {
            array.put(p.toJson())
        }
        prefs.edit().putString("profiles_list", array.toString()).apply()
    }

    private fun loadProfilesFromPrefs() {
        val prefs = getSharedPreferences("browser_profiles", MODE_PRIVATE)
        val raw = prefs.getString("profiles_list", null) ?: return
        profiles.clear()
        val array = JSONArray(raw)
        for (i in 0 until array.length()) {
            profiles.add(BrowserProfile.fromJson(array.getJSONObject(i)))
        }
    }

    override fun onPause() {
        super.onPause()
        activeWebView?.let {
            it.onPause()
            it.pauseTimers()
        }
        if (WebViewFeature.isFeatureSupported(WebViewFeature.MULTI_PROFILE)) {
            activeProfile?.let { profile ->
                ProfileStore.getInstance().getProfile(profile.id)?.cookieManager?.flush()
            }
        }
    }

    override fun onResume() {
        super.onResume()
        activeWebView?.let {
            it.onResume()
            it.resumeTimers()
        }
    }
}