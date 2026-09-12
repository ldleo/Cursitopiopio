package com.ldleo.isolatedbrowser

import org.json.JSONObject

data class DevicePreset(
    val name: String,
    val modelCode: String,
    val gpuVendor: String,
    val gpuRenderer: String,
    val userAgent: String
)

data class BrowserProfile(
    val id: String,
    var name: String,
    var startUrl: String,
    var seed: Int,
    var deviceName: String,
    var gpuVendor: String,
    var gpuRenderer: String,
    var userAgent: String
) {
    fun toJson(): JSONObject {
        val json = JSONObject()
        json.put("id", id)
        json.put("name", name)
        json.put("startUrl", startUrl)
        json.put("seed", seed)
        json.put("deviceName", deviceName)
        json.put("gpuVendor", gpuVendor)
        json.put("gpuRenderer", gpuRenderer)
        json.put("userAgent", userAgent)
        return json
    }

    companion object {
        fun fromJson(json: JSONObject): BrowserProfile {
            return BrowserProfile(
                id = json.getString("id"),
                name = json.getString("name"),
                startUrl = json.getString("startUrl"),
                seed = json.getInt("seed"),
                deviceName = json.optString("deviceName", "Samsung Galaxy S24 Ultra"),
                gpuVendor = json.getString("gpuVendor"),
                gpuRenderer = json.getString("gpuRenderer"),
                userAgent = json.optString("userAgent", "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36")
            )
        }

        // 15 Modelos Reales de Gama Media, Media-Alta y Alta
        val DEVICE_CATALOG = listOf(
            DevicePreset("Samsung Galaxy S24 Ultra", "SM-S928B", "Qualcomm", "Adreno (TM) 750", "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Samsung Galaxy S24", "SM-S921B", "Qualcomm", "Adreno (TM) 750", "Mozilla/5.0 (Linux; Android 14; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Samsung Galaxy S23 Ultra", "SM-S918B", "Qualcomm", "Adreno (TM) 740", "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Samsung Galaxy S23", "SM-S911B", "Qualcomm", "Adreno (TM) 740", "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Samsung Galaxy S22 Ultra", "SM-S908B", "Qualcomm", "Adreno (TM) 730", "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Xiaomi 14", "23127PN0CG", "Qualcomm", "Adreno (TM) 750", "Mozilla/5.0 (Linux; Android 14; 23127PN0CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Xiaomi 13 Pro", "2210132G", "Qualcomm", "Adreno (TM) 740", "Mozilla/5.0 (Linux; Android 14; 2210132G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Xiaomi POCO F6", "24069PC21G", "Qualcomm", "Adreno (TM) 735", "Mozilla/5.0 (Linux; Android 14; 24069PC21G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Xiaomi POCO F5 Pro", "23013PC75G", "Qualcomm", "Adreno (TM) 730", "Mozilla/5.0 (Linux; Android 14; 23013PC75G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Xiaomi POCO X6 Pro", "2311DRK48G", "ARM", "Mali-G615-MC6", "Mozilla/5.0 (Linux; Android 14; 2311DRK48G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Google Pixel 8 Pro", "Pixel 8 Pro", "ARM", "Mali-G715", "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Google Pixel 7 Pro", "Pixel 7 Pro", "ARM", "Mali-G710", "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("OnePlus 12", "CPH2581", "Qualcomm", "Adreno (TM) 750", "Mozilla/5.0 (Linux; Android 14; CPH2581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Motorola Edge 50 Pro", "motorola edge 50 pro", "Qualcomm", "Adreno (TM) 720", "Mozilla/5.0 (Linux; Android 14; motorola edge 50 pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36"),
            DevicePreset("Redmi Note 13 Pro+ 5G", "23090RA98G", "ARM", "Mali-G610 MC4", "Mozilla/5.0 (Linux; Android 14; 23090RA98G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Mobile Safari/537.36")
        )
    }
}