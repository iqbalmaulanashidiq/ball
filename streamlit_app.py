<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Kalkulator SPNL - Regula Falsi</title>

<!-- Library Math.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.min.js"></script>

<style>
    body {
        font-family: Arial, sans-serif;
        background: #f4f7f9;
        margin: 0;
        padding: 0;
    }

    .container {
        max-width: 1000px;
        margin: auto;
        padding: 20px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
        color: #1976D2;
    }

    .card {
        background: #fff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }

    .card h2 {
        margin-top: 0;
        color: #333;
    }

    input {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        border: 1px solid #ccc;
        border-radius: 8px;
    }

    .row {
        display: flex;
        gap: 15px;
    }

    .row input {
        flex: 1;
    }

    button {
        width: 100%;
        padding: 14px;
        background: #1976D2;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        margin-top: 10px;
    }

    button:hover {
        background: #145a9e;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }

    table, th, td {
        border: 1px solid #bbb;
    }

    th, td {
        padding: 8px;
        text-align: center;
    }

    .result {
        padding: 12px;
        background: #e8f5e9;
        border-left: 5px solid #43A047;
        margin-top: 10px;
        border-radius: 8px;
    }

    .error {
        padding: 12px;
        background: #FFEBEE;
        border-left: 5px solid #E53935;
        margin-top: 10px;
        border-radius: 8px;
    }
</style>
</head>

<body>

<div class="container">

    <h1>Kalkulator SPNL - Metode Regula Falsi</h1>

    <!-- Step 1 -->
    <div class="card">
        <h2>Step 1: Masukkan Persamaan</h2>
        <input type="text" id="fungsi" placeholder="contoh: x^3 - x - 2">
        <p id="preview"></p>
    </div>

    <!-- Step 2 -->
    <div class="card">
        <h2>Step 2: Pilih Interval</h2>
        <div class="row">
            <input type="number" id="a" placeholder="a">
            <input type="number" id="b" placeholder="b">
        </div>
        <p>f(a) = <span id="fa"></span></p>
        <p>f(b) = <span id="fb"></span></p>
        <p id="intervalInfo"></p>
    </div>

    <!-- Step 3 -->
    <div class="card">
        <h2>Step 3: Pengaturan Lanjut</h2>
        <input type="number" id="maxIter" value="50">
        <input type="number" id="tol" value="0.000001" step="0.000001">

        <button onclick="hitung()">Hitung Akar</button>
    </div>

    <div id="hasil"></div>
    <div id="tabel"></div>

</div>

<script>
// Preview fungsi
document.getElementById("fungsi").addEventListener("input", () => {
    document.getElementById("preview").innerHTML =
        "Anda memasukkan: f(x) = " + document.getElementById("fungsi").value;
});

// Update f(a) dan f(b)
["a", "b", "fungsi"].forEach(id => {
    document.getElementById(id).addEventListener("input", hitungFAFB);
});

function hitungFAFB() {
    let fn = document.getElementById("fungsi").value;
    let a = parseFloat(document.getElementById("a").value);
    let b = parseFloat(document.getElementById("b").value);

    if (!fn || isNaN(a) || isNaN(b)) return;

    try {
        let fa = math.evaluate(fn, {x: a});
        let fb = math.evaluate(fn, {x: b});

        document.getElementById("fa").innerText = fa;
        document.getElementById("fb").innerText = fb;

        if (fa * fb > 0) {
            document.getElementById("intervalInfo").innerHTML =
