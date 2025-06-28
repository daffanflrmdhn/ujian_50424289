

import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi status servis kendaraan
servis_db = {
    "B1234ABC": {"kendaraan": "Toyota Avanza", "status": "Sedang Dikerjakan", "mekanik": "Udin"},
    "D5678DEF": {"kendaraan": "Honda Vario", "status": "Menunggu Suku Cadang", "estimasi_selesai": "3 hari"},
    "F9012GHI": {"kendaraan": "Mitsubishi Pajero", "status": "Selesai, Siap Diambil", "total_biaya": 2500000},
    "B4321CBA": {"kendaraan": "Suzuki Ertiga", "status": "Antrean Pengecekan", "mekanik": "Joko"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-OTOJAYA] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/servis/<plat_nomor>/status', methods=['GET'])
def get_status_servis(plat_nomor):
    """Endpoint untuk mendapatkan status servis berdasarkan plat nomor."""
    log_server_activity(f"Permintaan status untuk plat: {plat_nomor}")
    
    time.sleep(random.uniform(0.3, 0.8)) 
    
    with db_lock:
        servis = servis_db.get(plat_nomor.upper())
    
    if servis:
        response_data = servis.copy()
        response_data["plat_nomor"] = plat_nomor.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Kendaraan dengan plat nomor tersebut tidak ada dalam antrean servis"}), 404

if __name__ == '__main__':
    log_server_activity("API Status Servis Bengkel OtoJaya dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)