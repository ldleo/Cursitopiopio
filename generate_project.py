import os

os.makedirs("app/src/main/java/com/ldleo/isolatedbrowser", exist_ok=True)
os.makedirs("app/src/main/res/layout", exist_ok=True)
os.makedirs("app/src/main/res/values", exist_ok=True)
os.makedirs("app/src/main/res/drawable", exist_ok=True)

with open("settings.gradle", "w") as f:
    f.write("""pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "Cursitopiopio"
include ':app'
""")

with open("build.gradle", "w") as f:
    f.write("""plugins {
    id 'com.android.application' version '8.2.2' apply false
    id 'org.jetbrains.kotlin.android' version '1.9.22' apply false
}
""")

with open("app/build.gradle", "w") as f:
    f.write("""plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    namespace 'com.ldleo.isolatedbrowser'
    compileSdk 34

    defaultConfig {
        applicationId "com.ldleo.isolatedbrowser"
        minSdk 26
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = '17'
    }
}

dependencies {
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    implementation 'androidx.webkit:webkit:1.12.1'
}
""")

with open("app/src/main/AndroidManifest.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <application
        android:allowBackup="true"
        android:icon="@android:drawable/sym_def_app_icon"
        android:label="Navegador"
        android:roundIcon="@android:drawable/sym_def_app_icon"
        android:supportsRtl="true"
        android:theme="@style/Theme.IsolatedBrowser"
        android:usesCleartextTraffic="true">
        <activity
            android:name=".MainActivity"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>""")

with open("app/src/main/res/values/strings.xml", "w") as f:
    f.write("""<resources>
    <string name="app_name">Navegador</string>
</resources>""")

with open("app/src/main/res/values/colors.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="bg_black">#0D0D0D</color>
    <color name="card_dark">#181818</color>
    <color name="card_border">#2C2C2C</color>
    <color name="text_primary">#F0F0F0</color>
    <color name="text_secondary">#8E8E93</color>
    <color name="accent_purple">#C5B3F9</color>
    <color name="accent_green">#34C759</color>
    <color name="accent_red">#FF453A</color>
</resources>""")

with open("app/src/main/res/values/themes.xml", "w") as f:
    f.write("""<resources>
    <style name="Theme.IsolatedBrowser" parent="Theme.Material3.Dark.NoActionBar">
        <item name="android:statusBarColor">@color/bg_black</item>
        <item name="android:navigationBarColor">@color/bg_black</item>
    </style>
</resources>""")

with open("app/src/main/res/drawable/bg_card.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/card_dark" />
    <corners android:radius="14dp" />
    <stroke android:width="1dp" android:color="@color/card_border" />
</shape>""")

with open("app/src/main/res/drawable/bg_input.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#242424" />
    <corners android:radius="10dp" />
    <stroke android:width="1dp" android:color="#383838" />
</shape>""")

with open("app/src/main/res/layout/activity_main.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="@color/bg_black">

    <LinearLayout
        android:id="@+id/ipBanner"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:background="#121212"
        android:padding="8dp"
        android:gravity="center_vertical">

        <TextView
            android:id="@+id/tvVpnStatus"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="🌐 Conectando a monitor de red..."
            android:textColor="@color/text_secondary"
            android:textSize="12sp" />

        <TextView
            android:id="@+id/btnRefreshIp"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="🔄"
            android:padding="4dp"
            android:textSize="14sp" />
    </LinearLayout>

    <LinearLayout
        android:id="@+id/topBar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:padding="10dp"
        android:background="@color/card_dark"
        android:gravity="center_vertical">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Navegador"
            android:textColor="@color/text_primary"
            android:textSize="18sp"
            android:textStyle="bold" />

        <View
            android:layout_width="0dp"
            android:layout_height="1dp"
            android:layout_weight="1" />

        <Button
            android:id="@+id/btnProfilesList"
            android:layout_width="wrap_content"
            android:layout_height="36dp"
            android:text="Perfiles"
            android:textSize="12sp"
            android:backgroundTint="#2C2C2E"
            android:textColor="@color/text_primary" />

        <Button
            android:id="@+id/btnCreateProfileTop"
            android:layout_width="wrap_content"
            android:layout_height="36dp"
            android:text="+ Nuevo"
            android:textSize="12sp"
            android:layout_marginStart="6dp"
            android:backgroundTint="@color/accent_purple"
            android:textColor="#000000" />
    </LinearLayout>

    <FrameLayout
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1">

        <LinearLayout
            android:id="@+id/profilesScreen"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical"
            android:gravity="center"
            android:padding="16dp">

            <TextView
                android:id="@+id/tvEmptyMessage"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Sin perfiles todavía"
                android:textColor="@color/text_secondary"
                android:textSize="18sp"
                android:layout_marginBottom="24dp" />

            <ScrollView
                android:id="@+id/scrollProfiles"
                android:layout_width="match_parent"
                android:layout_height="0dp"
                android:layout_weight="1"
                android:visibility="gone">
                <LinearLayout
                    android:id="@+id/llProfilesContainer"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical" />
            </ScrollView>

            <Button
                android:id="@+id/btnNewProfileBig"
                android:layout_width="match_parent"
                android:layout_height="50dp"
                android:text="+ Nuevo perfil"
                android:textColor="#000000"
                android:textStyle="bold"
                android:backgroundTint="@color/accent_purple" />
        </LinearLayout>

        <LinearLayout
            android:id="@+id/browserScreen"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical"
            android:visibility="gone">

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="horizontal"
                android:padding="8dp"
                android:background="#151515"
                android:gravity="center_vertical">

                <TextView
                    android:id="@+id/tvActiveBadge"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:text="Perfil Activo"
                    android:textColor="@color/accent_green"
                    android:textSize="12sp" />

                <Button
                    android:id="@+id/btnClearCurrentSession"
                    android:layout_width="wrap_content"
                    android:layout_height="32dp"
                    android:text="Limpiar y Salir"
                    android:textSize="11sp"
                    android:backgroundTint="@color/accent_red"
                    android:textColor="@color/text_primary" />
            </LinearLayout>

            <FrameLayout
                android:id="@+id/webViewContainer"
                android:layout_width="match_parent"
                android:layout_height="match_parent" />
        </LinearLayout>
    </FrameLayout>
</LinearLayout>""")

with open("app/src/main/res/layout/dialog_new_profile.xml", "w") as f:
    f.write("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="20dp"
    android:background="@drawable/bg_card">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Nuevo perfil"
        android:textColor="@color/text_primary"
        android:textSize="18sp"
        android:textStyle="bold"
        android:layout_marginBottom="14dp" />

    <EditText
        android:id="@+id/etProfileName"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:hint="Nombre del perfil (ej. Banco PT)"
        android:textColor="@color/text_primary"
        android:textColorHint="@color/text_secondary"
        android:background="@drawable/bg_input"
        android:padding="12dp"
        android:layout_marginBottom="12dp"
        android:textSize="14sp" />

    <EditText
        android:id="@+id/etProfileUrl"
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:hint="URL del sitio (https://...)"
        android:textColor="@color/text_primary"
        android:textColorHint="@color/text_secondary"
        android:background="@drawable/bg_input"
        android:padding="12dp"
        android:textSize="14sp"
        android:inputType="textUri" />

    <TextView
        android:id="@+id/tvUrlError"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="⚠️ URL inválida (incluye http:// o https://)"
        android:textColor="@color/accent_red"
        android:textSize="12sp"
        android:paddingTop="4dp"
        android:paddingBottom="4dp"
        android:visibility="gone" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Proxy (opcional)"
        android:textColor="@color/text_secondary"
        android:textSize="12sp"
        android:layout_marginTop="12dp"
        android:layout_marginBottom="4dp" />

    <TextView
        android:layout_width="match_parent"
        android:layout_height="48dp"
        android:text="Sin proxy (directo) - En próxima actualización"
        android:textColor="@color/text_secondary"
        android:background="@drawable/bg_input"
        android:gravity="center_vertical"
        android:padding="12dp"
        android:textSize="13sp" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:layout_marginTop="18dp">

        <Button
            android:id="@+id/btnSaveOnly"
            android:layout_width="0dp"
            android:layout_height="44dp"
            android:layout_weight="1"
            android:text="Guardar perfil"
            android:textSize="12sp"
            android:backgroundTint="#2C2C2E"
            android:textColor="@color/text_primary"
            android:layout_marginEnd="6dp" />

        <Button
            android:id="@+id/btnSaveAndOpen"
            android:layout_width="0dp"
            android:layout_height="44dp"
            android:layout_weight="1"
            android:text="Guardar y abrir"
            android:textSize="12sp"
            android:backgroundTint="@color/accent_purple"
            android:textColor="#000000" />
    </LinearLayout>

    <TextView
        android:id="@+id/btnCancelDialog"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="CANCELAR"
        android:textColor="@color/text_secondary"
        android:gravity="center"
        android:padding="12dp"
        android:textSize="13sp"
        android:textStyle="bold" />
</LinearLayout>""")

with open("app/src/main/java/com/ldleo/isolatedbrowser/StealthScript.kt", "w") as f:
    f.write("""package com.ldleo.isolatedbrowser

object StealthScript {
    fun generate(seed: Int, vendor: String, renderer: String): String {
        return \"\"\"
        (function() {
            try {
                const seed = $seed;

                Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8, configurable: false });
                Object.defineProperty(navigator, 'deviceMemory', { get: () => 8, configurable: false });
                Object.defineProperty(navigator, 'maxTouchPoints', { get: () => 5, configurable: false });
                Object.defineProperty(navigator, 'platform', { get: () => 'Linux aarch64', configurable: false });

                const fakeVendor = "$vendor";
                const fakeRenderer = "$renderer";

                function patchWebGL(proto) {
                    if (!proto) return;
                    const origGetParameter = proto.getParameter;
                    proto.getParameter = function(parameter) {
                        if (parameter === 37445) return fakeVendor;
                        if (parameter === 37446) return fakeRenderer;
                        return origGetParameter.apply(this, arguments);
                    };
                }
                patchWebGL(window.WebGLRenderingContext ? window.WebGLRenderingContext.prototype : null);
                patchWebGL(window.WebGL2RenderingContext ? window.WebGL2RenderingContext.prototype : null);

                const origToDataURL = HTMLCanvasElement.prototype.toDataURL;
                HTMLCanvasElement.prototype.toDataURL = function() {
                    const ctx = this.getContext('2d');
                    if (ctx && this.width > 0 && this.height > 0) {
                        try {
                            const imgData = ctx.getImageData(0, 0, Math.min(this.width, 10), Math.min(this.height, 10));
                            for (let i = 0; i < imgData.data.length; i += 4) {
                                imgData.data[i] = (imgData.data[i] + (seed % 9) + 1) % 256;
                            }
                            ctx.putImageData(imgData, 0, 0);
                        } catch(e) {}
                    }
                    return origToDataURL.apply(this, arguments);
                };

                const origGetImageData = CanvasRenderingContext2D.prototype.getImageData;
                CanvasRenderingContext2D.prototype.getImageData = function() {
                    const res = origGetImageData.apply(this, arguments);
                    if (res && res.data && res.data.length > 0) {
                        for (let i = 0; i < Math.min(res.data.length, 60); i += 4) {
                            res.data[i] = (res.data[i] + (seed % 9) + 1) % 256;
                        }
                    }
                    return res;
                };

                const nativeToString = Function.prototype.toString;
                const customToString = function() {
                    if (this === HTMLCanvasElement.prototype.toDataURL) {
                        return "function toDataURL() { [native code] }";
                    }
                    if (this === CanvasRenderingContext2D.prototype.getImageData) {
                        return "function getImageData() { [native code] }";
                    }
                    return nativeToString.apply(this, arguments);
                };
                Object.defineProperty(Function.prototype, 'toString', {
                    value: customToString,
                    configurable: false,
                    writable: false
                });
            } catch(e) {}
        })();
        \"\"\".trimIndent()
    }
}""")

with open("app/src/main/java/com/ldleo/isolatedbrowser/ProfileModel.kt", "w") as f:
    f.write("""package com.ldleo.isolatedbrowser

import org.json.JSONObject

data class BrowserProfile(
    val id: String,
    var name: String,
    var startUrl: String,
    val seed: Int,
    val gpuVendor: String,
    val gpuRenderer: String
) {
    fun toJson(): JSONObject {
        val json = JSONObject()
        json.put("id", id)
        json.put("name", name)
        json.put("startUrl", startUrl)
        json.put("seed", seed)
        json.put("gpuVendor", gpuVendor)
        json.put("gpuRenderer", gpuRenderer)
        return json
    }

    companion object {
        fun fromJson(json: JSONObject): BrowserProfile {
            return BrowserProfile(
                id = json.getString("id"),
                name = json.getString("name"),
                startUrl = json.getString("startUrl"),
                seed = json.getInt("seed"),
                gpuVendor = json.getString("gpuVendor"),
                gpuRenderer = json.getString("gpuRenderer")
            )
        }

        val GPU_LIST = listOf(
            Pair("Qualcomm", "Adreno (TM) 750"),
            Pair("Qualcomm", "Adreno (TM) 740"),
            Pair("Qualcomm", "Adreno (TM) 735"),
            Pair("Qualcomm", "Adreno (TM) 730"),
            Pair("Qualcomm", "Adreno (TM) 725"),
            Pair("Qualcomm", "Adreno (TM) 720"),
            Pair("Qualcomm", "Adreno (TM) 660"),
            Pair("Qualcomm", "Adreno (TM) 642L"),
            Pair("ARM", "Mali-G720-Immortalis MC12"),
            Pair("ARM", "Mali-G715-Immortalis MC11"),
            Pair("ARM", "Mali-G715 MC7"),
            Pair("ARM", "Mali-G710 MC10"),
            Pair("ARM", "Mali-G610 MC6"),
            Pair("ARM", "Mali-G77 MC9"),
            Pair("ARM", "Mali-G68 MC4"),
            Pair("ARM", "Mali-G57 MC2")
        )
    }
}""")

with open("app/src/main/java/com/ldleo/isolatedbrowser/MainActivity.kt", "w") as f:
    f.write("""package com.ldleo.isolatedbrowser

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
}""")
