#!usr/bin/env python
# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt
import mysql.connector
import json

host = 'mosquitto'
port = 1883
# iot/マックアドレス
# ※ラズパイは、ifconfigで確認してb8:27:ebから始まるもの
topic = 'iot/#'

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))  
  client.subscribe(topic)                         # subするトピックを設定 

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
  if  rc != 0:
    print("Unexpected disconnection.")

# メッセージが届いたときの処理
def on_message(client, userdata, msg):
  # msg.topicにトピック名が，msg.payloadに届いたデータ本体が入っている
  print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))

  data = json.loads(msg.payload.decode("utf-8"))
  temperature = data['temperature']
  humidity = data['humidity']
  measurement_at = data['measurement_at']

  print("temperature:{}".format(temperature))
  print("humidity:{}".format(humidity))
  print("measurement_at:{}".format(measurement_at))

  conn = mysql.connector.connect(
    host="db",
    user="root",
    passwd="VdwKsbe7rgM3",
    database="2019_grad_db"
  )
  cursor = conn.cursor()
  sql = "insert into dht11(temperature,humidity,measurement_at) values({},{},'{}')".format(temperature, humidity, measurement_at)
  cursor.execute(sql)
  cursor.close()
  conn.commit()
  conn.close()

if __name__ == '__main__':
  # MQTTの接続設定
  client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
  client.on_connect = on_connect         # 接続時のコールバック関数を登録
  client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
  client.on_message = on_message         # メッセージ到着時のコールバック

  client.connect(host, port, keepalive=60)  # 接続先は自分自身

  client.loop_forever()                  # 永久ループして待ち続ける

  
