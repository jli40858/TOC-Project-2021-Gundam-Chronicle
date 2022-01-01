from transitions.extensions import GraphMachine
from linebot.models import *
from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_usage(self, event):
        text = event.message.text
        return text.lower() == "主選單"

    def is_going_to_state0079(self, event):
        text = event.message.text
        return text.lower() == "0079"

    def is_going_to_state0083(self, event):
        text = event.message.text
        return text.lower() == "0083"

    def is_going_to_state0087(self, event):
        text = event.message.text
        return text.lower() == "0087"

    def is_going_to_state0079_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0079_rival(self, event):
        text = event.message.text
        return text.lower() == "吉翁"

    def is_going_to_state0083_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0083_rival(self, event):
        text = event.message.text
        return text.lower() == "吉翁殘黨"

    def is_going_to_state0087_main(self, event):
        text = event.message.text
        return text.lower() == "幽谷"

    def is_going_to_state0087_rival(self, event):
        text = event.message.text
        return text.lower() == "迪坦斯"

    def is_going_back(self, event):
        text = event.message.text
        return text.lower() == "返回"

    def on_enter_state0079(self, event):
        print("I'm entering state0079")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "宇宙世紀0078～0080年：\n\n一年戰爭\n\n離地球最遙遠的宇宙殖民地群「Side3」的市民要求自治權，以「吉翁公國」為名向地球聯邦發起的獨立戰爭。\n"
                          "本戰爭是人形機動兵器「機動戰士」首次投入實戰，且在戰爭初期就有全人類半數人口死亡。戰爭最終以支配吉翁公國的薩比家滅亡，新建的吉翁共和國臨時政府和地球聯邦政府簽訂終戰協定作結。\n"
                          "\n主要作品：\n《機動戰士鋼彈》\n（1979年 - 1980年）")

        buttons_template = TemplateSendMessage(
            alt_text='一年戰爭主要參戰勢力',
            template=ButtonsTemplate(
                title='一年戰爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/4mzE1yW.jpeg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='吉翁公國',
                        text='吉翁'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0083(self, event):
        print("I'm entering state0083")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "宇宙世紀0083年：\n\n迪拉茲紛爭\n\n吉翁公國軍的殘黨「迪拉茲艦隊」和地球聯邦軍間的紛爭。\n"
                          "紛爭的最後，地球北美農業地帶被迪拉茲艦隊的殖民地墜落作戰摧毀。以此為契機，聯邦內以「賈米托夫·海曼」准將為中心成立「迪坦斯」，開始強行鎮壓宇宙居民，造成日後「格利布斯戰役」的遠因。但整個紛爭事後被聯邦高層掩蓋，殖民地墜落被當成殖民地運送中發生的意外處理。\n\n主要作品：\n《機動戰士鋼彈0083：Stardust Memory》\n（1991年 - 1992年）")

        buttons_template = TemplateSendMessage(
            alt_text='迪拉茲紛爭主要參戰勢力',
            template=ButtonsTemplate(
                title='迪拉茲紛爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/E9kz7Nf.png',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='吉翁殘黨「迪拉茲艦隊」',
                        text='吉翁殘黨'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0087(self, event):
        print("I'm entering state0083")
        reply_token = event.reply_token
        send_text_message(reply_token, "宇宙世紀0087～0088年：\n\n格利布斯戰役\n\n"
                                       "為地球聯邦軍的內戰，以鎮壓宇宙居民為目的，由地球聯邦軍內地球至上主義者組成的軍閥「迪坦斯」和地球聯邦軍內對抗迪坦斯而組成的組織「幽谷」間的軍事衝突。\n"
                                       "戰役後期，從木星圈歸來的吉翁殘黨的攝政「哈曼·坎恩」率領的「阿克西斯」介入，三方陷入混戰，最終迪坦斯因失去領導階層而瓦解。\n\n主要作品：\n"
                                       "《機動戰士Z鋼彈》\n（1985年 - 1986年）")

        buttons_template = TemplateSendMessage(
            alt_text='格利布斯戰役主要參戰勢力',
            template=ButtonsTemplate(
                title='格利布斯戰役主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/b1VjB8m.jpg',
                actions=[
                    MessageTemplateAction(
                        label='幽谷',
                        text='幽谷'
                    ),
                    MessageTemplateAction(
                        label='迪坦斯',
                        text='迪坦斯'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0079_main(self, event):
        print("I'm entering state0079_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/XxRy2Qx.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/7FnqD2V.png')
        send_text_message(reply_token, "阿姆羅·雷（アムロ・レイ，Amuro Ray）\n\n是鋼彈系列作品當中由初代鋼彈開始登場的人物，同時也是《機動戰士鋼彈》的主角。他也作為《機動戰士鋼彈 "
                                       "逆襲的夏亞》的主角之一出現，此外，他也有在《機動戰士Z鋼彈》中以配角的方式登場，是鋼彈系列宇宙世紀中最重要的角色之一。\n\n駕駛之機體為RX-78-2 "
                                       "Gundam（鋼彈）")
        self.go_back()

    def on_enter_state0079_rival(self, event):
        print("I'm entering state0079_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/jl2kyVy.png')
        send_img(event.source.user_id, 'https://i.imgur.com/tEemUfd.jpeg')
        send_text_message(reply_token,
                          "夏亞·阿茲納布爾（シャア・アズナブル，Char Aznable）\n\n本名卡斯巴爾·雷姆·戴昆（キャスバル・レム・ダイクン，Casval Rem "
                          "Deikun），別名愛德華·瑪斯（エドワウ・マス，Édouard "
                          "Mass），是鋼彈系列宇宙世紀中最重要的角色之一。在《機動戰士鋼彈》的一年戰爭中，夏亞被稱作紅色彗星（赤い彗星）\n\n駕駛之機體為MS-06S Char's Zaku "
                          "II（夏亞專用薩克 II）。")
        self.go_back()

    def on_enter_state0083_main(self, event):
        print("I'm entering state0083_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/zjSi23q.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/Y3ah1ir.jpg')
        send_text_message(reply_token, "浦木宏 （コウ・ウラキ）\n\n是地球聯邦軍澳洲特林頓基地所屬MS測試駕駛員，故事的男主角，也是GUNDAM系列作品當中首位以正規軍人身份登場的主角。軍銜為少尉。稱號為「幻之擊墜王」。\n\n駕駛之機體為 RX-78GP01 Gundam Zephyranthes（鋼彈試作1號機）")
        self.go_back()

    def on_enter_state0083_rival(self, event):
        print("I'm entering state0083_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/blLP0U8.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/Pvfd6x9.png')
        send_text_message(reply_token, "阿納貝爾·卡多（アナベル・ガトー，Anavel Gato）\n\n吉翁公國殘黨迪拉茲艦隊所屬的王牌駕駛員，25歲，身高195cm。一年戰爭時期軍階為大尉，迪拉茲紛爭時期為少佐，基連·薩比的追隨者。稱號為「所羅門的噩夢」\n\n駕駛之機體為RX-78GP02A Gundam Physalis（鋼彈試作2號機）")
        self.go_back()

    def on_enter_state0087_main(self, event):
        print("I'm entering state0087_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/HXEazS9.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/9vcxc02.jpg')
        send_text_message(reply_token, "卡密兒·維丹（カミーユ・ビダン，Kamille Bidan）\n\n是最早在鋼彈系列架空紀元宇宙世紀動畫《機動戰士Z 鋼彈》中登場的虛構人物，在宇宙世紀的舞台上有「最強的新人類」（最高のニュータイプ）之稱。是為鋼彈系列有史以來新人類能力最強的少年。官方設定身高168.2cm，體重59.5kg，血液為AB型。\n\n駕駛之機體為MSZ-006 Zeta Gundam（Z鋼彈）")
        self.go_back()

    def on_enter_state0087_rival(self, event):
        print("I'm entering state0087_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/37Hvn0Q.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/osjnFcd.jpg')
        send_text_message(reply_token, "帕普迪馬斯·希羅克（パプテマス・シロッコ，Paptimus Scirocco）\n\n，機動戰士Z 鋼彈中的登場人物。地球聯邦政府木星資源採探船諸比多理斯（ジュピトリス）的艦長，軍階為上尉，劇場版為上校。木星氦3（熱核反應爐主要燃料）採探艦隊的指揮官。\n\n駕駛之機體為PMX-003 The-O")
        self.go_back()

    def on_enter_user(self, event):
        print("I'm entering user")
        reply_token = event.reply_token
        buttons_template = TemplateSendMessage(
            alt_text='鋼彈歷年戰役資訊查詢',
            template=ButtonsTemplate(
                title='鋼彈歷年戰役資訊查詢',
                text='請選擇欲查詢之宇宙世紀年（Universal Century, U.C）',
                thumbnail_image_url='https://i.imgur.com/TeMdZOR.png',
                actions=[
                    MessageTemplateAction(
                        label='UC.0079',
                        text='0079'
                    ),
                    MessageTemplateAction(
                        label='UC.0083',
                        text='0083'
                    ),
                    MessageTemplateAction(
                        label='UC.0087',
                        text='0087'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_usage(self, event):
        print("I'm entering usage")
        reply_token = event.reply_token
        buttons_template = TemplateSendMessage(
            alt_text='鋼彈歷年戰役資訊查詢',
            template=ButtonsTemplate(
                title='鋼彈歷年戰役資訊查詢',
                text='請選擇欲查詢之宇宙世紀年（Universal Century, U.C）',
                thumbnail_image_url='https://i.imgur.com/TeMdZOR.png',
                actions=[
                    MessageTemplateAction(
                        label='UC.0079',
                        text='0079'
                    ),
                    MessageTemplateAction(
                        label='UC.0083',
                        text='0083'
                    ),
                    MessageTemplateAction(
                        label='UC.0087',
                        text='0087'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()
