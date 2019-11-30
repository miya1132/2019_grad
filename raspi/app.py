#!usr/bin/env python
# -*- coding: utf-8 -*- 

from time import sleep
import paho.mqtt.client as mqtt
import json
import uuid
import struct
from datetime import datetime

host = '192.168.1.9'
port = 1883
# iot/マックアドレス
# ※ラズパイは、ifconfigで確認してb8:27:ebから始まるもの
topic = 'iot/{}'

# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))

# ブローカーが切断したときの処理
def on_disconnect(client, userdata, flag, rc):
  if rc != 0:
     print("Unexpected disconnection.")

# publishが完了したときの処理
def on_publish(client, userdata, mid):
  print("publish: {0}".format(mid))

def main():
  mac = "-".join([hex(fragment)[2:].zfill(2)
              for fragment in struct.unpack("BBBBBB", struct.pack("!Q", uuid.getnode())[2:])])

  client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
  client.on_connect = on_connect         # 接続時のコールバック関数を登録
  client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
  client.on_publish = on_publish         # メッセージ送信時のコールバック

  client.connect(host, port, keepalive=60)  # 接続先は自分自身

  # 通信処理スタート
  client.loop_start()                     # subはloop_forever()だが，pubはloop_start()で起動だけさせる

  # 永久に繰り返す
  while True:
    now = datetime.now()
    data = {
      "temperature":29.0,
      "humidity":35,
      "measurement_at":now.strftime("%Y/%m/%d %H:%M:%S")
    }
    
    client.publish(topic.format(mac), json.dumps(data))    # トピック名とメッセージを決めて送信
    sleep(3)   # 3秒待つ

if __name__ == "__main__":
  main()
