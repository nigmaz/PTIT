from flask import Flask, request
import requests
import json
import config
import component as com
from chatty import Chatty
import os, sys, requests, json
from flask import Flask, request, jsonify
from flask import Flask, request
import requests
from pymessenger import Bot

app = Flask(__name__)


VERIFY_TOKEN = "ma_xac_nhan_ung_dung"
PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN
PAT = config.PAGE_ACCESS_TOKEN
bot = Bot(PAGE_ACCESS_TOKEN)
token_dict = {"access_token": PAGE_ACCESS_TOKEN}
fb_api = "https://graph.facebook.com/v4.0/me/messages"
# to get the user's details, such as name, profile picture, location etc. we use facebook graph messenger profile API.
profile_api = "https://graph.facebook.com/v4.0/me/messenger_profile"
# this is a generic link for facebook graph API. It is useless as it is. I have concetenated links with it to use for myself in the code.
psid_url = "https://graph.facebook.com/"

# =================================================================================================
detail1 = "🌟 THÔNG TIN SẢN PHẨM:💥 Áo Khoác Kaki M620 (EMO) với Chất liệu Kaki Hàn 2 lớp mềm mịn cực mát🌀 Size: L (1m40-60 40-60kg);\nXL (1m55-70 55-70kg).\n🌀 Màu sắc: Y hình\n🌀Đường may kỹ, tinh tế, sắc xảo.\n🌀 Form chuẩn Unisex Nam Nữ Couple đều mặc được.\n🌀 Giao hàng tận nơi. Nhận hàng rồi thanh toán."
product1_image = "https://cf.shopee.vn/file/292530a2cbb57306df29b49067a52023"
detail2 = "Áo Khoác Nhung Tăm Thêu Chữ CHOOSE ❤ Áo BomBer Bóng Chày Nam Nữ Phong Cách Hàn Quốc\n- chất liệu: nhung tăm(ko quá dày,cũng ko quá mỏng,loại 1 lớp)\n- style: Hàn Quốc Oppa\n- diện trong các dịp: tiệc tùng, cưới hỏi, chụp hình, du lich, đi chơi, cafe cho đến hẹn hò..."
product2_image = "https://cf.shopee.vn/file/b16eea1f4d4e44564b5934e88e326704"
detail3 = "(A) độ tuổi nộp đơn là 18-24 tuổi;\nChất liệu polyester;\n(A) một kích thước cho mỗi kích thước;\nVải polyester;\nPhong cách ngọt ngào;\n(A) trẻ em có mũ trùm đầu;\n(B) khóa sừng của nắp cửa hàng may mặc;"
product3_image = "https://cf.shopee.vn/file/13f24b86391e1f3d4cab432296fd5856"
detail4 = "Kiểu dáng: Đường phố cá tính / Harajuku \ nChi tiết kiểu quần áo: dây kéo \ n Phiên bản quần áo: rời \ n Hình thức kết hợp: một chiếc \ n Chiều dài áo: dài tay \ n Kiểu dáng: giản dị \ n Kiểu cổ áo: Mũ trùm đầu \ n Độ tuổi áp dụng: thanh niên (18-25 tuổi) \ nMùa danh sách: Mùa thu năm 2020"
product4_image = "https://cf.shopee.vn/file/9a3acc48f7f7f7eee14e10274ac24fb6"
detail5 = "🎁THÔNG TIN SẢN PHẨM : \v- Màu sắc : nhiều màu\n- Kích thước : freesize 75kg\n- Chất liệu : Nỉ bông"
product5_image = "https://cf.shopee.vn/file/ba3232efcb5294ae9c3ffd91691d1400"
detail6 = "Phong cách: ngọt ngào và tươi mát / Nhật Bản\nYếu tố phổ biến / thủ công: màu tinh khiết\nLoại phiên bản quần áo: rời\nPhong cách mặc: áo nịt\nHình thức kết hợp: mảnh đơn"
product6_image = "https://cf.shopee.vn/file/4549f2b7e6df70daf8eba1f13b94e5e5"
detail7 = "Chất liệu: Len\nMẫu: Sọc"
product7_image = "https://cf.shopee.vn/file/0774792ea53f998eb4ad34e63cc761bb_tn"
detail8 = "Áo khoác nhung tăm lót lông vừa xinh vừa rẻ \nÁo có 2 màu : be và Hồng ạ\nÁo freesize dưới 75kg nha chị em"
product8_image = "https://cf.shopee.vn/file/acc65dd858ab21c8f9d223a21dbde6a5"
order = "cám ơn bạn đã đặt hàng, shop sẽ tiến hành liên hệ sớm nhất với bạn để hoàn tất thủ tục !"
link_shopee = "https://shopee.vn/buitrungcuong12?categoryId=100017&itemId=13726002565"
shopee_image = "https://deo.shopeemobile.com/shopee/shopee-mobilemall-live-sg/assets/d010b985fc1475e559b6db819889703c.png"
# =================================================================================

# In order to show a message, quick reply or gallery, we have to send JSONs to our app.
# Below is the complete json to show the main gallery in the Digiskills chatbot.
carousel_json = {
    "message": {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "[S03] Áo khoác kaki hai lớp nam",
                        "image_url": product1_image,
                        "subtitle": "₫149.000",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product1 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product1 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": " Áo Khoác Nhung Thêu Chữ CHOOSE Unisex Form Rộng",
                        "image_url": product2_image,
                        "subtitle": "₫159.000",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product2 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product2 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "❤Áo Khoác Lông Có Mũ Tai Mèo Thời Trang Thu Đông Cho Nữ",
                        "image_url": product3_image,
                        "subtitle": "₫624.900",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product3 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product3 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "Áo Khoác Nữ Vải Nhung Dày Thời Trang Mùa Đông 2020",
                        "image_url": product4_image,
                        "subtitle": "₫450.000",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product4 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product4 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "Áo khoác nỉ bomber nam nữ",
                        "image_url": product5_image,
                        "subtitle": "₫99.000 - ₫118.000",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product5 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product5 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "Áo Khoác Cardigan Dài Tay Dễ Thương Học Sinh",
                        "image_url": product6_image,
                        "subtitle": "₫148.000 - ₫189.000",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product6 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product6 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "Áo khoác len cardigan kẻ viền vàng học sinh quốc tế Hàn Quốc",
                        "image_url": product7_image,
                        "subtitle": "320,000 đ",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product7 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product7 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "Áo khoác nhung tăm lót lông",
                        "image_url": product8_image,
                        "subtitle": "₫360.000",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "___ asked product8 details",
                                "title": "Chi tiết sản phẩm",
                            },
                            {
                                "type": "postback",
                                "title": "Hình ảnh cho sản phẩm",
                                "payload": "___ asked product8 image",
                            },
                            {
                                "type": "postback",
                                "title": "Đặt hàng",
                                "payload": "___ asked order",
                            },
                        ],
                    },
                    {
                        "title": "Tham quan gian hàng Shoppe:",
                        "image_url": shopee_image,
                        "subtitle": "",
                        "buttons": [
                            {
                                "type": "postback",
                                "payload": "tham_quan",
                                "title": "Thăm quan",
                            },
                            {
                                "type": "postback",
                                "payload": "tiep_tuc_chat",
                                "title": "Tiếp tục chat",
                            },
                        ],
                    },
                ],
            },
        }
    }
}


@app.route("/", methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return "Not connected!"
    elif request.method == "POST":
        if "hub.mode" in request.args:
            mode = request.args.get("hub.mode")
            print(mode)
        if "hub.verify_token" in request.args:
            token = request.args.get("hub.verify_token")
            print(token)
        if "hub.challenge" in request.args:
            challenge = request.args.get("hub.challenge")
            print(challenge)

        if "hub.mode" in request.args and "hub.verify_token" in request.args:
            mode = request.args.get("hub.mode")
            token = request.args.get("hub.verify_token")

            if mode == "subscribe" and token == VERIFY_TOKEN:
                print("WEBHOOK VERIFIED")

                challenge = request.args.get("hub.challenge")

                return challenge, 200
            else:
                return "ERROR", 403

        # ===========================================
        data = request.get_json()
        if data["object"] == "page":
            entries = data["entry"]
            for entry in entries:
                webhookEvent = entry["messaging"][0]
                print(webhookEvent)
                senderPsid = webhookEvent["sender"]["id"]
                print("Sender PSID: {}".format(senderPsid))
                messaging = entry["messaging"]
                temp_id = entry["id"]
            # getting the sender ID
            for messaging_event in messaging:
                sender_id = messaging_event["sender"]["id"]
                # getting the receiver ID
                recipient_id = messaging_event["recipient"]["id"]
                # using a GET request to extract the user's information. In the below lines of code, we get the name of the user. Now, we can call the user by his name.

                if temp_id != sender_id:
                    response = requests.get(
                        psid_url
                        + sender_id
                        + "?fields=name&access_token="
                        + PAGE_ACCESS_TOKEN
                    )
                    # user_json = json.loads(response.content)
                    # user_name = user_json["name"]
                webhookEvent = entry["messaging"][0]
                print(webhookEvent)
                senderPsid = webhookEvent["sender"]["id"]
                print("Sender PSID: {}".format(senderPsid))
                if messaging_event.get("postback"):
                    #   xử lí event postback
                    if (
                        messaging_event["postback"].get("payload")
                        == "___ asked product1 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail1},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product1 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product1_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product2 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail2},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product2 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product2_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product3 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail3},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product3 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product3_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product4 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail4},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product4 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product4_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product5 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail5},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product5 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product5_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product6 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail6},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product6 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product6_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product7 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail7},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product7 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )
                        com.send_img(sender_id, product7_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product8 details"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": detail8},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif (
                        messaging_event["postback"].get("payload")
                        == "___ asked product8 image"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": "ảnh của sản phẩm"},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                        com.send_img(sender_id, product8_image)

                    elif (
                        messaging_event["postback"].get("payload") == "___ asked order"
                    ):
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": order},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    if messaging_event["postback"].get("payload") == "tham_quan":
                        response = requests.post(
                            fb_api,
                            params=token_dict,
                            json={
                                "message": {"text": link_shopee},
                                "recipient": {"id": sender_id},
                                "notification_type": "REGULAR",
                                "messaging_type": "RESPONSE",
                            },
                        )

                    elif messaging_event["postback"].get("payload") == "tiep_tuc_chat":
                        gen_carousel(sender_id)
                    gen_continue_button(sender_id)
                # ===============================================================
                elif messaging_event.get("message"):
                    if messaging_event["message"].get("quick_reply"):
                        if (
                            messaging_event["message"]["quick_reply"].get("payload")
                            == "___ clicked generic continue"
                        ):
                            gen_carousel(sender_id)
                        if (
                            messaging_event["message"]["quick_reply"].get("payload")
                            == "tham_quan"
                        ):
                            response = requests.post(
                                fb_api,
                                params=token_dict,
                                json={
                                    "message": {"text": link_shopee},
                                    "recipient": {"id": sender_id},
                                    "notification_type": "REGULAR",
                                    "messaging_type": "RESPONSE",
                                },
                            )
                    # HANDLE NORMAL MESSAGES HERE
                    elif messaging_event["message"].get("text"):
                        # HANDLE TEXT MESSAGES
                        handleMessage(senderPsid, webhookEvent["message"])
                        gen_continue_button(sender_id)
                return "EVENT_RECEIVED", 200
        else:
            return "ERROR", 404


def gen_carousel(id):
    carousel_json["recipient"] = {"id": id}
    response = requests.post(
        fb_api,
        params=token_dict,
        json={
            "message": {"text": "Tiếp tục\nHãy tham khảo các sản phẩm của chúng tôi"},
            "recipient": {"id": id},
            "notification_type": "REGULAR",
            "messaging_type": "RESPONSE",
        },
    )
    response2 = requests.post(fb_api, params=token_dict, json=carousel_json)


def gen_continue_button(id):
    response2 = requests.post(
        fb_api,
        params=token_dict,
        json={
            "recipient": {"id": id},
            "messaging_type": "RESPONSE",
            "message": {
                "text": "Bấm Continue để tiếp tục\n👇👇👇",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Continue",
                        "payload": "___ clicked generic continue",
                    }
                ],
            },
        },
    )


def gen_link_shopee_button(id):
    response2 = requests.post(
        fb_api,
        params=token_dict,
        json={
            "recipient": {"id": id},
            "messaging_type": "RESPONSE",
            "message": {
                "text": "Ghé thăm gian hàng shopee của chúng tôi:",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Ghé thăm",
                        "payload": "tham_quan",
                    }
                ],
            },
        },
    )


# def welcome_msg(id, niggas_name):
# 	response = requests.post(fb_api,params=token_dict, json={"message": {"text": welcome_message + niggas_name + " Nice to meet you. 😊\nDigiSkills Chatbot at your service 🤖"}, "recipient": {"id": id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
# 	response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": id}, "messaging_type": "RESPONSE","message":{"text": "You can ask me about DigiSkills Training program.","quick_replies":[{"content_type":"text","title":"Next","payload":"___ clicked next"}]}})


# =======================================================================================================
def callSendAPI(senderPsid, response):
    PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN

    payload = {
        "recipient": {"id": senderPsid},
        "message": response,
        "messaging_type": "RESPONSE",
    }
    headers = {"content-type": "application/json"}

    url = "https://graph.facebook.com/v10.0/me/messages?access_token={}".format(
        PAGE_ACCESS_TOKEN
    )
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)


# ===========================================================================================================
# Function for handling a message from MESSENGER
def handleMessage(senderPsid, receivedMessage):
    data = request.get_json()
    sender_id = data["entry"][0]["messaging"][0]["sender"]["id"]
    req = requests.get(
        "https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}".format(
            sender_id, PAT
        )
    )
    user_data = req.json()
    if user_data.get("first_name"):
        f_name = user_data["first_name"]
        l_name = user_data["last_name"]
        p_pic = user_data["profile_pic"]
    # check if received message contains text
    print("We entered the HANDLE MESSAGE FUNCTION")
    if "text" in receivedMessage:
        print("TEXT does exist in the RECEIVER MESSAGE")
        toSend = receivedMessage["text"]
        greeting = ["xin chào", "bạn có ở đó không?", "hi", "hello", "hey", "ya"]

        if toSend.lower() in greeting:
            com.send_message(
                sender_id,
                "Hi {} {}, Chào mừng bạn ghé thăm Python Shop.Hãy gửi cho chúng tôi bất kỳ câu hỏi nào của bạn!!".format(
                    l_name, f_name
                ),
            )

            com.send_message(sender_id, "Hãy tham khảo một số sản phẩm của shop:")
            com.send_img(
                sender_id, "https://cf.shopee.vn/file/943849ee53628608fded6e0fe5b15c74"
            )
            com.send_img(
                sender_id, "https://cf.shopee.vn/file/d6d2f6f5afd89c612fc980b481655da4"
            )
            com.send_img(
                sender_id, "https://cf.shopee.vn/file/2f6bf9ae032e6cdddb62b78499535e53"
            )

        elif toSend == "send image":
            com.send_message(sender_id, "Đây là ảnh đại diện của bạn:")
            com.send_img(sender_id, p_pic)

        else:
            # #The Chatbot function ------------------------
            chatbot = Chatty()
            chatbotResponse = chatbot.chatbot_response(toSend)
            print("The Chatbot Response is: {}".format(chatbotResponse))
            response = {"text": chatbotResponse}
            callSendAPI(senderPsid, response)
    else:
        response = {
            "text": "Xin lỗi bạn nhưng chúng tôi chỉ chấp nhận tin nhắn text. Các tệp đính kèm sẽ không được cháp nhận. Hãy thử lại!"
        }
        callSendAPI(senderPsid, response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)
