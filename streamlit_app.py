<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Kalkulator SPNL - Regula Falsi</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
<style>
    body {
        font-family: 'Poppins', sans-serif;
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

    <!-- Hasil -->
    <div id="hasil"></div>

    <!-- Tabel Iterasi -->
    <div id="tabel"></div>

</div>

<script>
    // UPDATE PREVIEW FUNGSI
    document.getElementById("fungsi").addEventListener("input", () => {
        document.getElementById("preview").innerHTML =
            "Anda memasukkan: f(x) = " + document.getElementById("fungsi").value;
    });

    // UPDATE f(a) DAN f(b)
    document.getElementById("a").addEventListener("input", hitungFAFB);
    document.getElementById("b").addEventListener("input", hitungFAFB);
    document.getElementById("fungsi").addEventListener("input", hitungFAFB);

    function hitungFAFB() {
        let fn = document.getElementById("fungsi").value;
        let a = parseFloat(document.getElementById("a").value);
        let b = parseFloat(document.getElementById("b").value);

        try {
            let fa = math.evaluate(fn, {x: a});
            let fb = math.evaluate(fn, {x: b});

            document.getElementById("fa").innerText = fa;
            document.getElementById("fb").innerText = fb;

            if (fa * fb > 0) {
                document.getElementById("intervalInfo").innerHTML =
                    "<div class='error'>Interval tidak valid: f(a) dan f(b) tidak bertanda berbeda.</div>";
            } else {
                document.getElementById("intervalInfo").innerHTML =
                    "<div class='result'>Interval valid ✓</div>";
            }

        } catch {
            document.getElementById("fa").innerText = "";
            document.getElementById("fb").innerText = "";
        }
    }

    // METODE REGULA FALSI
    function hitung() {
        let fn = document.getElementById("fungsi").value;
        let a = parseFloat(document.getElementById("a").value);
        let b = parseFloat(document.getElementById("b").value);
        let maxIter = parseInt(document.getElementById("maxIter").value);
        let tol = parseFloat(document.getElementById("tol").value);

        let fa = math.evaluate(fn, {x: a});
        let fb = math.evaluate(fn, {x: b});

        let iterasi = [];
        let xrOld = 0, xr = 0;

        for (let i = 1; i <= maxIter; i++) {
            xr = (a*fb - b*fa) / (fb - fa);
            let fxr = math.evaluate(fn, {x: xr});

            iterasi.push([i, a, b, xr, fxr, Math.abs(xr - xrOld)]);
            
            if (Math.abs(xr - xrOld) < tol) break;

            if (fa * fxr < 0) {
                b = xr;
                fb = fxr;
            } else {
                a = xr;
                fa = fxr;
            }

            xrOld = xr;
        }

        // TAMPILKAN HASIL
        document.getElementById("hasil").innerHTML = `
            <div class="card">
                <h2>Hasil Perhitungan</h2>
                <div class="result">
                    Akar mendekati: <b>${xr}</b><br>
                    Error: ${Math.abs(xr - xrOld)}<br>
                    Iterasi total: ${iterasi.length}
                </div>
            </div>
        `;

        // TAMPILKAN TABEL
        let tabelHTML = `
            <div class="card">
            <h2>Tabel Iterasi</h2>
            <table>
                <tr>
                    <th>Iterasi</th><th>a</th><th>b</th>
                    <th>x_r</th><th>f(x_r)</th><th>Error</th>
                </tr>
        `;

        iterasi.forEach(row => {
            tabelHTML += `
                <tr>
                    <td>${row[0]}</td>
                    <td>${row[1]}</td>
                    <td>${row[2]}</td>
                    <td>${row[3]}</td>
                    <td>${row[4]}</td>
                    <td>${row[5]}</td>
                </tr>`;
        });

        tabelHTML += "</table></div>";

        document.getElementById("tabel").innerHTML = tabelHTML;
    }
</script>

</body>
</html>
