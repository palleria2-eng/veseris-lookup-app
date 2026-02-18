<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Veseris UV Insect Lamp Cross-Reference Tool – Complete official guide. Select brand and model to instantly see the correct UV lamp and Veseris stock codes." />
  <title>Veseris UV Insect Lamp Cross-Reference Tool</title>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  
  <style>
    .tail-container { max-width: 1100px; margin: 0 auto; }
    .select-style {
      width: 100%;
      padding: 0.75rem 1rem;
      border: 1px solid #d1d5db;
      border-radius: 0.75rem;
      font-size: 1.125rem;
      outline: none;
    }
    .select-style:focus {
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .result-card { animation: fadeIn 0.4s ease forwards; }
  </style>
</head>
<body class="bg-gradient-to-br from-blue-50 to-white min-h-screen font-sans antialiased">

  <div class="tail-container p-6 md:p-10">

    <!-- Header -->
    <div class="text-center mb-10">
      <img
        src="https://veseris.com/media/logo/default/veseris-logo.png"
        alt="Veseris Logo"
        class="mx-auto h-20 md:h-28 object-contain"
        onerror="this.src='https://via.placeholder.com/300x80?text=Veseris+Logo';"
      />
      <p class="mt-3 text-sm text-gray-600">Official Veseris UV Insect Lamp Cross-Reference Tool</p>
    </div>

    <!-- Title -->
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-4 bg-white shadow-lg px-8 py-4 rounded-2xl">
        <i class="fa-solid fa-lightbulb text-5xl text-yellow-500"></i>
        <div>
          <h1 class="text-4xl md:text-5xl font-bold tracking-tight text-gray-900">Veseris Lamp Finder</h1>
          <p class="text-blue-600 font-semibold text-xl mt-1">UV Insect Trap Cross-Reference Guide</p>
        </div>
      </div>
      <p class="mt-6 text-gray-700 max-w-2xl mx-auto text-lg">
        Complete data from the official Veseris UV Insect Lamp Cross Reference Guide.<br>
        Select brand → model → get exact lamp type, code &amp; stock numbers.
      </p>
    </div>

    <!-- Selection -->
    <div class="bg-white rounded-3xl shadow-2xl p-8 mb-12">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
            <i class="fa-solid fa-building text-blue-600 text-xl"></i>
            STEP 1: Select Brand / Company
          </label>
          <select id="brand" class="select-style"></select>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
            <i class="fa-solid fa-box text-emerald-600 text-xl"></i>
            STEP 2: Select Product / Model
          </label>
          <select id="model" disabled class="select-style">
            <option value="">First select a brand...</option>
          </select>
        </div>
      </div>

      <div class="mt-10 text-center">
        <button onclick="resetTool()"
                class="inline-flex items-center gap-2 px-8 py-4 bg-gray-200 hover:bg-gray-300 rounded-2xl text-gray-800 font-semibold transition-colors shadow-sm">
          <i class="fa-solid fa-rotate"></i> Reset Selections
        </button>
      </div>
    </div>

    <!-- Result -->
    <div id="result" class="hidden bg-white rounded-3xl shadow-2xl overflow-hidden result-card">
      <div class="bg-gradient-to-r from-blue-700 to-emerald-700 text-white px-8 py-8 flex flex-col sm:flex-row items-center justify-between gap-6">
        <div>
          <p class="text-sm uppercase tracking-wide opacity-90 font-medium">Selected Model</p>
          <h2 id="selected-title" class="text-2xl md:text-3xl font-bold"></h2>
        </div>
        <div class="text-right">
          <p id="lamp-code-big" class="text-4xl md:text-5xl font-mono font-extrabold tracking-widest"></p>
        </div>
      </div>

      <div class="p-8 md:p-10">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <!-- Lamp Details -->
          <div class="lg:col-span-1">
            <div class="bg-gray-50 rounded-2xl p-6 h-full border border-gray-100">
              <h3 class="uppercase text-xs font-semibold tracking-widest text-gray-500 mb-4">Lamp Details</h3>
              <div id="lamp-type" class="text-xl font-semibold mb-6 text-gray-800"></div>
              <div class="space-y-5 text-sm">
                <div>
                  <span class="block text-xs text-gray-500 uppercase tracking-wide">Lamp Code</span>
                  <span id="lamp-code" class="font-mono text-2xl font-bold text-emerald-700"></span>
                </div>
                <div>
                  <span class="block text-xs text-gray-500 uppercase tracking-wide">Case Quantity</span>
                  <span id="case-qty" class="text-2xl font-semibold text-gray-800"></span>
                </div>
              </div>
            </div>
          </div>

          <!-- Stock Codes -->
          <div class="lg:col-span-2">
            <h3 class="uppercase text-xs font-semibold tracking-widest text-gray-500 mb-5">Veseris Stock Codes</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div class="border border-gray-200 rounded-2xl p-6 bg-white shadow-sm">
                <div class="flex items-center gap-3 mb-4">
                  <i class="fa-solid fa-circle text-emerald-500"></i>
                  <span class="font-semibold text-lg">Regular</span>
                </div>
                <table class="w-full text-sm">
                  <tr class="border-b"><td class="py-3 text-gray-600">Case</td><td id="reg-case" class="font-mono text-right font-bold"></td></tr>
                  <tr><td class="py-3 text-gray-600">Each</td><td id="reg-each" class="font-mono text-right font-bold"></td></tr>
                </table>
              </div>

              <div class="border border-gray-200 rounded-2xl p-6 bg-white shadow-sm">
                <div class="flex items-center gap-3 mb-4">
                  <i class="fa-solid fa-shield-halved text-amber-500"></i>
                  <span class="font-semibold text-lg">Shatterproof</span>
                </div>
                <table class="w-full text-sm">
                  <tr class="border-b"><td class="py-3 text-gray-600">Case</td><td id="shat-case" class="font-mono text-right font-bold"></td></tr>
                  <tr><td class="py-3 text-gray-600">Each</td><td id="shat-each" class="font-mono text-right font-bold"></td></tr>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-gray-50 px-8 py-5 text-xs text-gray-500 border-t flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>Data imported from <strong>Veseris UV Insect Lamp Cross Reference Guide.xlsx</strong> • Accurate as of February 2026</div>
        <a href="#" onclick="window.location.reload(); return false;" class="hover:text-blue-700 flex items-center gap-2 transition-colors">
          <i class="fa-solid fa-arrow-rotate-right"></i> New Search
        </a>
      </div>
    </div>

    <!-- Footer -->
    <div class="text-center text-sm text-gray-500 mt-16">
      Digital version of the classic Veseris cross-reference wheel.<br>
      For latest pricing, availability, or updates contact Veseris or your representative.
    </div>

  </div>

  <script>
    // ===============================================
    // FULL Veseris UV Lamp Cross-Reference Data
    // Imported directly from the official Excel file
    // ===============================================
    const crossRefData = {
      "AP & G Vector": [
        { model: "Vector 15", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Vector 30", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Classic", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "911 Dynamite (2012 model)", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "Vector Discreet", lamp_type: "26 Watt Lynx 2 pin", lamp_code: "CFQ 26W", reg_case: "802129", reg_each: "802130", shat_case: "N/A", shat_each: "N/A", case_qty: "50" },
        { model: "Plasma", lamp_type: "36 Watt 16\" - CFL", lamp_code: "CFL36WBL", reg_case: "802099", reg_each: "802098", shat_case: "802101", shat_each: "802100", case_qty: "10" },
        { model: "Plasma I", lamp_type: "36 Watt 16\" - CFL", lamp_code: "CFL36WBL", reg_case: "802099", reg_each: "802098", shat_case: "802101", shat_each: "802100", case_qty: "10" },
        { model: "911 Dynamite (2013 model)", lamp_type: "36 Watt 16\" - CFL", lamp_code: "CFL36WBL", reg_case: "802099", reg_each: "802098", shat_case: "802101", shat_each: "802100", case_qty: "10" }
      ],
      "Brandenburg/Pelsis": [
        { model: "Genus Eclipse", lamp_type: "15 Watt 12\" - T5", lamp_code: "F15T5BL", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "835219", case_qty: "25" },
        { model: "Genus Eclipse Ultra", lamp_type: "15 Watt 12\" - T5", lamp_code: "F15T5BL", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "835219", case_qty: "25" },
        { model: "Genus Illume Alpha/Galaxy", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Genus Orbit", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Genus Jet", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Genus Orbit Innova", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Genus Fli", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Genus Vortex ", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Genus Illume Galaxy", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "Genus Spectra", lamp_type: "36 Watt 16\" - CFL", lamp_code: "CFL36WBL", reg_case: "802099", reg_each: "802098", shat_case: "802101", shat_each: "802100", case_qty: "10" },
        { model: "Genus Spectra Compact", lamp_type: "36 Watt 16\" - CFL", lamp_code: "CFL36WBL", reg_case: "802099", reg_each: "802098", shat_case: "802101", shat_each: "802100", case_qty: "10" }
      ],
      "Envirolights": [
        { model: "Flylight Junior", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" }
      ],
      "Gardner": [
        { model: "UCT-15", lamp_type: "15 Watt 12\" - T5", lamp_code: "F15T5BL", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "835219", case_qty: "25" },
        { model: "WS-85", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "GT-180", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "FL-215", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "FL-30 Accent", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "GT-215", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "FL-40P", lamp_type: "20 Watt 24\" - T8", lamp_code: "F20T8BL", reg_case: "N/A", reg_each: "N/A", shat_case: "843174", shat_each: "825205", case_qty: "25" },
        { model: "ANA-40", lamp_type: "20 Watt 24\" - T8", lamp_code: "F20T8BL", reg_case: "N/A", reg_each: "N/A", shat_case: "843174", shat_each: "825205", case_qty: "25" },
        { model: "GT-220SS", lamp_type: "20 Watt 24\" - T8", lamp_code: "F20T8BL", reg_case: "N/A", reg_each: "N/A", shat_case: "843174", shat_each: "825205", case_qty: "25" },
        { model: "AG-963S", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "AG-961S", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "AG-969S", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "WS-95", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "GT-200", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "WS-225", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "AG-970S", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "AG-661S", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "AG-241S", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "RG-1002S", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "GT-480", lamp_type: "40 Watt 48\" - T8", lamp_code: "F40T8BL", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "825206", case_qty: "25" },
        { model: "FL-65P", lamp_type: "40 Watt 48\" - T8", lamp_code: "F40T8BL", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "825206", case_qty: "25" },
        { model: "FlyWeb FW-9", lamp_type: "9 Watt PL", lamp_code: "PL-9W", reg_case: "732507", reg_each: "N/A", shat_case: "N/A", shat_each: "N/A", case_qty: "50" }
      ],
      "Gilbert": [
        { model: "1999GT Flying Venus", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "225GT Sticky Fox", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "219GT Sticky Tiger", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "601GT Sticky Lizard", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "601TJ Junior", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "2000GT Flying Venus", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "2002GT Flying Venus", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "2004GT Leonardo DaTrapi", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "220 Guerrilla", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "601D-GT Sticky Don", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "747GT Sticky Bear", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "601E Executive", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "601T The Don", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "711 Flying Lion", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "711SS Stainless Flying Lion", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "705 Night Hawk", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "605 Night Eagle", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" },
        { model: "607 Hall Stalker ", lamp_type: "40 Watt 48\" - T12", lamp_code: "F40T12BL", reg_case: "784682", reg_each: "679694", shat_case: "784560", shat_each: "741664", case_qty: "25" }
      ],
      "Pelsis": [
        { model: "Edge", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Intellientlight Pro", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Halo 15", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Halo 30", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Halo 45", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Halo Aqua", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Flytrap Professional 30", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Halo Curve", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Nectar", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Luralite Professional", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Satelite 30", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "PlusZap 30", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Allure", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Exocutor 30", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Exocutor 40", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "Aura", lamp_type: "22W Circline", lamp_code: "F22W T9", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "845317", case_qty: "12" },
        { model: "Exocutor 80", lamp_type: "36 Watt 24\" - T8", lamp_code: "F36T8", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "845318", case_qty: "N/A" },
        { model: "Flytrap Professional 80", lamp_type: "40 Watt 24\" - T12", lamp_code: "F40T12BL", reg_case: "N/A", reg_each: "N/A", shat_case: "802096", shat_each: "802097", case_qty: "25" },
        { model: "Excalibur Aqua 80", lamp_type: "40 Watt 24\" - T12", lamp_code: "F40T12BL", reg_case: "N/A", reg_each: "N/A", shat_case: "802096", shat_each: "802097", case_qty: "25" }
      ],
      "Pest West": [
        { model: "Titan Alpha", lamp_type: "15 Watt 12\" - T5", lamp_code: "F15T5BL", reg_case: "N/A", reg_each: "N/A", shat_case: "N/A", shat_each: "835219", case_qty: "25" },
        { model: "Mantis 1x2", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Mantis 2x2", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Mantis Uplight", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Titan 300", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Mantis 1x2 IP", lamp_type: "15 Watt 18\" - T8", lamp_code: "F15T8BL", reg_case: "717568", reg_each: "802398", shat_case: "717571", shat_each: "824984", case_qty: "25" },
        { model: "Chameleon EXG", lamp_type: "20 Watt 24\" - T12", lamp_code: "F20T12BL", reg_case: "784562", reg_each: "657857", shat_case: "784561", shat_each: "775672", case_qty: "25" },
        { model: "Mantis 1x2 Max 50", lamp_type: "25 Watt 18\" - T8", lamp_code: "F25T8BL", reg_case: "802107", reg_each: "670131", shat_case: "802109", shat_each: "775671", case_qty: "25" },
        { model: "Mantis Uplight Max 36", lamp_type: "36 Watt 16\" - CFL", lamp_code: "CFL36WBL", reg_case: "802099", reg_each: "802098", shat_case: "802101", shat_each: "802100", case_qty: "10" },
        { model: "Nemesis CM", lamp_type: "40 Watt 24\" - T12", lamp_code: "F40T12BL", reg_case: "N/A", reg_each: "N/A", shat_case: "802096", shat_each: "802097", case_qty: "25" },
        { model: "Mantis 4x4 EX", lamp_type: "40 Watt 24\" - T12", lamp_code: "F40T12BL", reg_case: "N/A", reg_each: "N/A", shat_case: "802096", shat_each: "802097", case_qty: "25" },
        { model: "Mantis 4x4", lamp_type: "40 Watt 24\" - T12", lamp_code: "F40T12BL", reg_case: "N/A", reg_each: "N/A", shat_case: "802096", shat_each: "802097", case_qty: "25" }
      ]
    };

    // Populate brands (sorted alphabetically)
    function populateBrands() {
      const brandSelect = document.getElementById("brand");
      brandSelect.innerHTML = '<option value="">Choose a brand...</option>';
      
      const sortedBrands = Object.keys(crossRefData).sort();
      sortedBrands.forEach(brand => {
        const option = document.createElement("option");
        option.value = brand;
        option.textContent = brand;
        brandSelect.appendChild(option);
      });
    }

    // Brand changed → populate models
    document.getElementById("brand").addEventListener("change", function () {
      const brand = this.value;
      const modelSelect = document.getElementById("model");
      const resultDiv = document.getElementById("result");

      modelSelect.innerHTML = '<option value="">Select model...</option>';
      resultDiv.classList.add("hidden");

      if (brand && crossRefData[brand]) {
        const sortedModels = [...crossRefData[brand]].sort((a, b) => a.model.localeCompare(b.model));
        sortedModels.forEach(entry => {
          const option = document.createElement("option");
          option.value = entry.model;
          option.textContent = entry.model;
          modelSelect.appendChild(option);
        });
        modelSelect.disabled = false;
      } else {
        modelSelect.disabled = true;
      }
    });

    // Model changed → show result
    document.getElementById("model").addEventListener("change", function () {
      const brand = document.getElementById("brand").value;
      const modelName = this.value;
      if (!brand || !modelName) return;

      const entry = crossRefData[brand].find(e => e.model === modelName);
      if (entry) showResult(brand, entry);
    });

    function showResult(brand, entry) {
      document.getElementById("selected-title").innerHTML = `${entry.model} <span class="text-sm font-normal opacity-75">— ${brand}</span>`;
      document.getElementById("lamp-code-big").textContent = entry.lamp_code;
      document.getElementById("lamp-type").innerHTML = `<span class="text-gray-500 text-sm block mb-1 font-medium uppercase">TYPE</span>${entry.lamp_type}`;
      document.getElementById("lamp-code").textContent = entry.lamp_code;
      document.getElementById("case-qty").textContent = entry.case_qty === "N/A" ? "N/A (contact Veseris)" : `${entry.case_qty} per case`;

      document.getElementById("reg-case").textContent = entry.reg_case;
      document.getElementById("reg-each").textContent = entry.reg_each;
      document.getElementById("shat-case").textContent = entry.shat_case;
      document.getElementById("shat-each").textContent = entry.shat_each;

      // Style N/A entries
      document.querySelectorAll("#reg-case, #reg-each, #shat-case, #shat-each").forEach(el => {
        if (el.textContent.trim() === "N/A") {
          el.classList.add("text-gray-400", "line-through");
        } else {
          el.classList.remove("text-gray-400", "line-through");
        }
      });

      const resultDiv = document.getElementById("result");
      resultDiv.classList.remove("hidden");
      resultDiv.scrollIntoView({ behavior: "smooth", block: "center" });
    }

    function resetTool() {
      document.getElementById("brand").value = "";
      document.getElementById("model").innerHTML = '<option value="">First select a brand...</option>';
      document.getElementById("model").disabled = true;
      document.getElementById("result").classList.add("hidden");
    }

    // Initialize
    window.onload = populateBrands;
  </script>
</body>
</html>
