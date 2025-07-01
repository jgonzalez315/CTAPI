from flask import Flask, request
import os
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(silent=True)

        print("\n📩 Webhook recibido:")
        print(json.dumps(data, indent=2) if data else "⚠️ Webhook sin contenido")

        if data:
            # Ruta por defecto
            ruta_archivo = os.path.abspath("estado_trx.json")

            # Si es una devolución, guardar en otro archivo
            if data.get("transactionType") == "devolucion":
                ruta_archivo = os.path.abspath("devolucion_trx.json")

            print(f"📝 Guardando archivo en: {ruta_archivo}")
            with open(ruta_archivo, "w") as f:
                json.dump(data, f)

            print("✅ Webhook guardado exitosamente.")
        else:
            print("⚠️ Webhook sin datos válidos.")

        return "", 200

    except Exception as e:
        print(f"❌ Error al procesar el webhook: {e}")
        return "Error interno", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)



