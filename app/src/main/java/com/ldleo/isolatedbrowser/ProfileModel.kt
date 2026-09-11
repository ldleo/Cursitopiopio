package com.ldleo.isolatedbrowser

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
}