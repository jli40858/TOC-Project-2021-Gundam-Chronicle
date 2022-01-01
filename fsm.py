from transitions.extensions import GraphMachine
from linebot.models import *
from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_page2(self, event):
        text = event.message.text
        return text.lower() == "到第二頁"

    def is_going_to_page3(self, event):
        text = event.message.text
        return text.lower() == "到第三頁"

    def is_going_back_to_page1(self, event):
        text = event.message.text
        return text.lower() == "回第一頁"

    def is_going_to_page1_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_page2_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_page3_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0079(self, event):
        text = event.message.text
        return text.lower() == "0079"

    def is_going_to_state0083(self, event):
        text = event.message.text
        return text.lower() == "0083"

    def is_going_to_state0087(self, event):
        text = event.message.text
        return text.lower() == "0087"

    def is_going_back_page1(self, event):
        text = event.message.text
        return text.lower() == "返回"

    def is_going_back_page2(self, event):
        text = event.message.text
        return text.lower() == "返回"

    def is_going_back_page3(self, event):
        text = event.message.text
        return text.lower() == "返回"

    def is_going_to_state0079_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0079_rival(self, event):
        text = event.message.text
        return text.lower() == "吉翁"

    def is_going_to_state0079_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0083_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0083_rival(self, event):
        text = event.message.text
        return text.lower() == "吉翁殘黨"

    def is_going_to_state0083_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0087_main(self, event):
        text = event.message.text
        return text.lower() == "幽谷"

    def is_going_to_state0087_rival(self, event):
        text = event.message.text
        return text.lower() == "迪坦斯"

    def is_going_to_state0087_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0088(self, event):
        text = event.message.text
        return text.lower() == "0088"

    def is_going_to_state0093(self, event):
        text = event.message.text
        return text.lower() == "0093"

    def is_going_to_state0096(self, event):
        text = event.message.text
        return text.lower() == "0096"

    def is_going_to_state0088_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0088_rival(self, event):
        text = event.message.text
        return text.lower() == "新吉翁"

    def is_going_to_state0088_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0093_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0093_rival(self, event):
        text = event.message.text
        return text.lower() == "新吉翁"

    def is_going_to_state0093_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0096_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0096_rival(self, event):
        text = event.message.text
        return text.lower() == "帶袖的"

    def is_going_to_state0096_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0123(self, event):
        text = event.message.text
        return text.lower() == "0123"

    def is_going_to_state0133(self, event):
        text = event.message.text
        return text.lower() == "0133"

    def is_going_to_state0153(self, event):
        text = event.message.text
        return text.lower() == "0153"

    def is_going_to_state0123_main(self, event):
        text = event.message.text
        return text.lower() == "聯邦"

    def is_going_to_state0123_rival(self, event):
        text = event.message.text
        return text.lower() == "骷髏尖兵"

    def is_going_to_state0123_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0133_main(self, event):
        text = event.message.text
        return text.lower() == "新骷髏尖兵"

    def is_going_to_state0133_rival(self, event):
        text = event.message.text
        return text.lower() == "木星帝國"

    def is_going_to_state0133_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_state0153_main(self, event):
        text = event.message.text
        return text.lower() == "神聖軍事同盟"

    def is_going_to_state0153_rival(self, event):
        text = event.message.text
        return text.lower() == "贊斯卡爾帝國"

    def is_going_to_state0153_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

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
        print("I'm entering state0087")
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

    def on_enter_state0079_menu(self, event):
        print("I'm entering state0079_menu")
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

    def on_enter_state0083_menu(self, event):
        print("I'm entering state0083_menu")
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

    def on_enter_state0087_menu(self, event):
        print("I'm entering state0087_menu")
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
        self.go_back()

    def on_enter_state0088(self, event):
        print("I'm entering state0088")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "宇宙世紀0088～0089年：\n\n第一次新吉翁抗爭\n\n吉翁公國軍殘黨「阿克西斯」改組成的「新吉翁」與格利布斯戰役的勝利者「幽谷」的戰爭。\n"
                          "後期，新吉翁因夏亞調略葛雷米分裂內鬥而弱化，實質指導者的攝政「哈曼·坎恩」戰死，吉翁勢力失去小行星阿克西斯。\n\n提及作品：\n《機動戰士鋼彈ZZ》\n（1986年 - "
                          "1987年）")

        buttons_template = TemplateSendMessage(
            alt_text='第一次新吉翁抗爭主要參戰勢力',
            template=ButtonsTemplate(
                title='第一次新吉翁抗爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/GVMncUx.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='新吉翁',
                        text='新吉翁'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0093(self, event):
        print("I'm entering state0093")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "宇宙世紀0093年：\n\n第二次新吉翁抗爭\n\n吉翁國父「吉翁·茲姆·戴昆」之子「卡斯巴爾·雷姆·戴昆（夏亞·阿茲納布爾）」組成的「新吉翁」對地球聯邦政府發起的叛亂。\n\n "
                          "提及作品：\n《機動戰士鋼彈 逆襲的夏亞》\n（1988年）")

        buttons_template = TemplateSendMessage(
            alt_text='第二次新吉翁抗爭主要參戰勢力',
            template=ButtonsTemplate(
                title='第二次新吉翁抗爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/e0ABIRy.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='新吉翁',
                        text='新吉翁'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0096(self, event):
        print("I'm entering state0096")
        reply_token = event.reply_token
        send_text_message(reply_token, "宇宙世紀0096年：\n\n第三次新吉翁抗爭\n\n在第二次新吉翁戰爭——別名「逆襲的夏亞」——終結後，地球圈取得短暫的和平。這之後3年，宇宙世紀0096"
                                       "年，在工業殖民地「工業7號」上進行一項秘密交涉。和地球聯邦政府有秘密協議並依此發展的「畢斯特財團」，打算將過去用以威脅聯邦的最高機密「拉普拉斯之盒」交給新吉翁的殘黨軍「帶袖的」。一場圍繞拉普拉斯之盒的戰爭就此展開。\n\n提及作品：\n《機動戰士鋼彈UC》\n（2010年 - 2014年）")
        buttons_template = TemplateSendMessage(
            alt_text='第三次新吉翁抗爭主要參戰勢力',
            template=ButtonsTemplate(
                title='第三次新吉翁抗爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/v5UIzVH.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='新吉翁殘黨「帶袖的」',
                        text='帶袖的'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0088_main(self, event):
        print("I'm entering state0088_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/IFjX9iS.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/gX7MnI1.png')
        send_text_message(reply_token, "傑特·亞希達（ジュドー·アーシタ，Judau Ashta）\n\n是《機動戰士鋼彈ZZ》中登場的人物。本故事的主角，面對逆境仍然與夥伴樂觀以對的新類型人少年。聲優是矢尾一樹。故事開始時是14歲，血型是B型，身高165cm，重56kg。\n\n駕駛之機體為MSZ-010 ΖΖ Gundam（ZZ鋼彈）")
        self.go_back()

    def on_enter_state0088_rival(self, event):
        print("I'm entering state0088_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/kX8tLZT.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/BWBg9Fh.jpg')
        send_text_message(reply_token,
                          "哈曼·卡恩（ハマーン・カーン，Haman Karn）\n\n非常剛強高傲，平常説話非常簡短乾脆。給人一種實幹家的印象。優秀的洞察力和高智慧，冷靜及判斷力兼備。然也會一時頭腦發熱不顧前後而行事。很強的責任感。她天真温柔的性格由於背叛的原因被埋藏在內心的深處。\n\n駕駛之機體為AMX-004 Qubeley（邱貝雷）")
        self.go_back()

    def on_enter_state0088_menu(self, event):
        buttons_template = TemplateSendMessage(
            alt_text='第一次新吉翁抗爭主要參戰勢力',
            template=ButtonsTemplate(
                title='第一次新吉翁抗爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/GVMncUx.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='新吉翁',
                        text='新吉翁'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_state0093_main(self, event):
        print("I'm entering state0093_main")
        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/BlV7uZa.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/RnlhT24.jpg')
        send_text_message(reply_token, "阿姆羅·雷（アムロ・レイ，Amuro Ray）\n\n是鋼彈系列作品當中由初代鋼彈開始登場的人物，同時也是《機動戰士鋼彈》的主角。他也作為《機動戰士鋼彈 "
                                       "逆襲的夏亞》的主角之一出現，此外，他也有在《機動戰士Z鋼彈》中以配角的方式登場，是鋼彈系列宇宙世紀中最重要的角色之一。\n\n駕駛之機體為RX-93 ν Gundam（Nu鋼彈）")
        self.go_back()

    def on_enter_state0093_rival(self, event):
        print("I'm entering state0093_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/ihOAitF.png')
        send_img(event.source.user_id, 'https://i.imgur.com/TCvxURw.jpg')
        send_text_message(reply_token,
                          "夏亞·阿茲納布爾（シャア・アズナブル，Char Aznable）\n\n本名卡斯巴爾·雷姆·戴昆（キャスバル・レム・ダイクン，Casval Rem "
                          "Deikun），別名愛德華·瑪斯（エドワウ・マス，Édouard "
                          "Mass），是鋼彈系列宇宙世紀中最重要的角色之一。在《機動戰士鋼彈》的一年戰爭中，夏亞被稱作紅色彗星（赤い彗星）\n\n駕駛之機體為MSN-04 Sazabi"
                          "（沙薩比）。")
        self.go_back()

    def on_enter_state0093_menu(self, event):
        print("I'm entering state0093_menu")
        buttons_template = TemplateSendMessage(
            alt_text='第二次新吉翁抗爭主要參戰勢力',
            template=ButtonsTemplate(
                title='第二次新吉翁抗爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/e0ABIRy.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='新吉翁',
                        text='新吉翁'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_state0096_main(self, event):
        print("I'm entering state0096_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/WRwrXaI.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/apl27Bi.jpg')
        send_text_message(reply_token, "巴納吉·林克斯（バナージ・リンクス，Banagher Links）\n\n《機動戰士鋼彈UC》小説及OVA作品中的男主角，16歲的少年，擁有深褐色的瞳孔及頭髮，帶有古老東洋血統的膚色，亞納海姆電子工業專科學校工學部資源開發科的實習學生，其真正身份為卡帝亞斯·畢斯特的私生子。\n\n駕駛之機體為RX-0 Unicorn Gundam（獨角獸鋼彈）。")
        self.go_back()

    def on_enter_state0096_rival(self, event):
        print("I'm entering state0096_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/u30sPe7.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/1eqnlzx.jpg')
        send_text_message(reply_token, "弗爾·伏朗托（フル・フロンタル，Full Frontal）\n\n新吉翁殘黨「帶袖的」之最高領導，戴假面不以真面目示人。其機體以及作戰風格（不穿宇航服）和平時的表現（無論是頭髮的顏色、面具還是說話時的聲線以及用詞）與夏亞如出一轍，因此人稱「紅色彗星夏亞再臨」。\n\n駕駛之機體為MSN-06S Sinanju（新安洲）")
        self.go_back()

    def on_enter_state0096_menu(self, event):
        print("I'm entering state0096_menu")
        buttons_template = TemplateSendMessage(
            alt_text='第三次新吉翁抗爭主要參戰勢力',
            template=ButtonsTemplate(
                title='第三次新吉翁抗爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/v5UIzVH.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='新吉翁殘黨「帶袖的」',
                        text='帶袖的'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_state0123(self, event):
        print("I'm entering state0123")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "宇宙世紀0123年： \n\n宇宙巴比倫建國戰爭\n\n經過短暫的和平後，貴族主義在宇宙殖民地的政治界和商界中抬頭，當中羅那家族更組成一支私立軍隊「骷髏尖兵」。地球聯邦軍一直對宇宙民居採取觀察態度，並沒有加以理會。U.C.0123年，骷髏尖兵部隊突襲Side 4各宇宙殖民地，與地球聯邦軍部隊交戰。地球聯邦軍的機動戰士的性能不及骷髏尖兵的機動戰士，戰爭處於一面倒的狀態。宇宙殖民地FRONTIER IV的某間大學內正在進行選美比賽，正當裁判宣佈謝西莉勝出時，一架被毀的機動戰士掉下來，會場頓時陷入恐慌。主角西布克和他的朋友集合後前往戰爭博物館避難，但他們眼見地球聯邦軍節節敗退，於是決定駕駛的半毀的舊式機動戰士，想逃往24號港口乘搭難民船……。\n\n提及作品：\n《機動戰士鋼彈F91》\n（1991年）")
        buttons_template = TemplateSendMessage(
            alt_text='宇宙巴比倫建國戰爭主要參戰勢力',
            template=ButtonsTemplate(
                title='宇宙巴比倫建國戰爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/snyZTQY.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='骷髏尖兵',
                        text='骷髏尖兵'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0133(self, event):
        print("I'm entering state0133")
        reply_token = event.reply_token
        send_text_message(reply_token,
                          "宇宙世紀0133年：\n\n木星戰役\n\n故事講述發生在宇宙巴比倫建國戰爭後10年（U.C.0133年），一場已經在蠢蠢欲動的戰爭。\n\n來自地球圈的交換留學生托比亞，在即將抵達留學目的地木星圈時，竟遇上了宇宙海盜襲擊，並目睹了傳說中海盜的機動戰士，「鋼彈」。 危急之際，托比亞擅自駕駛機動戰士迎戰鋼彈，在機體即將被破壞時，海盜卻示意要自己逃生。驚訝於海盜不殺人的托比亞逃往附近船艦，意外發現到這艘木星前往地球的運輸船內竟裝滿了毒氣。在即將被木星特務滅口的危機下，鋼彈再次出現並救了托比亞。面對滿懷疑惑的托比亞，鋼彈的駕駛員打開了面罩，報出了自己的名號『骷髏尖兵－金凱杜·那烏』……\n\n提及作品：\n《機動戰士海盜鋼彈》\n（1994年- 1997年）")

        buttons_template = TemplateSendMessage(
            alt_text='木星戰役主要參戰勢力',
            template=ButtonsTemplate(
                title='木星戰役主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/3foqDym.jpg',
                actions=[
                    MessageTemplateAction(
                        label='新骷髏尖兵',
                        text='新骷髏尖兵'
                    ),
                    MessageTemplateAction(
                        label='木星帝國',
                        text='木星帝國'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0153(self, event):
        print("I'm entering state0153")
        reply_token = event.reply_token
        send_text_message(reply_token, "宇宙世紀0153年：\n\n贊斯卡爾戰爭\n\nU.C.0140年，受到「殖民地主義」抬頭下，各宇宙殖民地為了確立自治權的權利，紛紛建立各自的勢力，脫離地球聯邦軍的統治，於是宇宙戰國時代正式爆發。贊斯卡爾帝國為了擴展勢力，更以建立新秩序為理由向地球聯邦軍宣戰，為了抵抗贊斯卡爾帝國的侵略，由原屬地球聯邦軍士兵、亞納海姆公司成員和民間組織組成「神聖軍事同盟」的組織，利用「鋼彈」的名氣，在不同據點進行開發新型機動戰士—「V鋼彈」去抵抗贊斯卡爾帝國的攻擊。\n主要作品：\n《機動戰士V鋼彈》\n（1993年 - 1994年）")

        buttons_template = TemplateSendMessage(
            alt_text='贊斯卡爾戰爭主要參戰勢力',
            template=ButtonsTemplate(
                title='贊斯卡爾戰爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/Hh59ZNh.jpg',
                actions=[
                    MessageTemplateAction(
                        label='神聖軍事同盟',
                        text='神聖軍事同盟'
                    ),
                    MessageTemplateAction(
                        label='贊斯卡爾帝國',
                        text='贊斯卡爾帝國'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_state0123_main(self, event):
        print("I'm entering state0123_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/K0nc0i0.png')
        send_img(event.source.user_id, 'https://i.imgur.com/ZfIHUqe.png')
        send_text_message(reply_token, "西布克·亞諾（シーブック・アノー，Seabook Arno）\n\n為《機動戰士鋼彈》系列動畫電影《機動戰士鋼彈F91》、系列漫畫《機動戰士海盜鋼彈》等作品中登場之架空人物。為《機動戰士鋼彈F91》的主角。男性，於動畫《機動戰士鋼彈F91》本篇中登場時年齡為17歲，於漫畫《機動戰士海盜鋼彈》中登場時年齡為28歲，動畫聲優為辻谷耕史。\n\n駕駛之機體為F91 Gundam F91（鋼彈F91）")
        self.go_back()

    def on_enter_state0123_rival(self, event):
        print("I'm entering state0123_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/zKcjpgN.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/PISwK4A.jpg')
        send_text_message(reply_token,
                          "鐵假面\n\n本名為卡羅索·羅納（カロッゾ・ロナ Karozzo Rona），45歲，羅納家族的女婿，賽西莉的父親。早年妻子娜迪亞與部下私奔一事令他深受打擊，自此只能戴上面具掩飾自卑的心理。奉行「貴族主義」的野心家。\n\n駕駛之機體為XMA-01 Rafflesia（拉芙蕾西亞）")
        self.go_back()

    def on_enter_state0123_menu(self, event):
        print("I'm entering state0123_menu")
        buttons_template = TemplateSendMessage(
            alt_text='宇宙巴比倫建國戰爭主要參戰勢力',
            template=ButtonsTemplate(
                title='宇宙巴比倫建國戰爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/snyZTQY.jpg',
                actions=[
                    MessageTemplateAction(
                        label='地球聯邦軍',
                        text='聯邦'
                    ),
                    MessageTemplateAction(
                        label='骷髏尖兵',
                        text='骷髏尖兵'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_state0133_main(self, event):
        print("I'm entering state0133_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/o23gDew.png')
        send_img(event.source.user_id, 'https://i.imgur.com/Q39RUQp.png')
        send_text_message(reply_token, "托比亞·亞羅納克斯（トビア・アロナクス，Tobia Arronax）\n\n15歲，本故事的主角之一，擁有很大潛能的新人類。本為地球圈前往木星圈的交換留學生，但遇到宇宙海盜後發現了木星帝國的秘密，因此決定加入骷髏尖兵，一起對抗木星帝國。故事前期只負責駕駛小兵機，在金凱杜的教導下和新人類能力覺醒後，成為新骷髏尖兵軍的主力之一，故事後期在別的貴族主義支持派中取得骨十字鋼彈X3，並與木星帝國的總統，古拉克斯·杜加奇進行決戰。\n\n駕駛之機體為 XM-X3 Crossbone Gundam X-3（骨十字鋼彈X-3）")
        self.go_back()

    def on_enter_state0133_rival(self, event):
        print("I'm entering state0133_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/CNaGep7.jpg')
        send_img(event.source.user_id, 'https://i.imgur.com/Jm61c3Y.jpg')
        send_text_message(reply_token, "薩比尼·夏爾（ザビーネ・シャル，Zabine Chareux）\n\n為宇宙巴比倫帝國骷髏尖兵的菁英，但對帝國的慘酷作法不滿而背叛，加入了貝拉一行人。但其貴族主義的思想到加入新骷髏尖兵後仍沒有改變，認定「貝拉·羅納」是統領人類的最佳人選，所以連金凱杜也不完全信任他。\n\n駕駛之機體為XM-X2 Crossbone Gundam X-2（骨十字鋼彈X-2）")
        self.go_back()

    def on_enter_state0133_menu(self, event):
        print("I'm entering state0133_menu")
        buttons_template = TemplateSendMessage(
            alt_text='木星戰役主要參戰勢力',
            template=ButtonsTemplate(
                title='木星戰役主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/3foqDym.jpg',
                actions=[
                    MessageTemplateAction(
                        label='新骷髏尖兵',
                        text='新骷髏尖兵'
                    ),
                    MessageTemplateAction(
                        label='木星帝國',
                        text='木星帝國'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_state0153_main(self, event):
        print("I'm entering state0153_main")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/Qfi8j2t.png')
        send_img(event.source.user_id, 'https://i.imgur.com/w2CT30g.png')
        send_text_message(reply_token, "胡索·艾溫（ウッソ・エヴィン，Uso Ewin）\n\n是《機動戰士V鋼彈》中登場的人物。本故事中的主角，在宇宙世紀所登場的主角中，是最年輕的駕駛員（13嵗，與《機動戰士鋼彈AGE》第三世代主角奇歐·明日野同齡）。聲優是阪口大助。\n\n駕駛之機體為LM312V04 Victory Gundam（V鋼彈）")
        self.go_back()

    def on_enter_state0153_rival(self, event):
        print("I'm entering state0153_rival")

        reply_token = event.reply_token
        send_img(event.source.user_id, 'https://i.imgur.com/uoTui9z.png')
        send_img(event.source.user_id, 'https://i.imgur.com/fGOgYqb.png')
        send_text_message(reply_token, "克羅諾克爾·艾夏（クロノクル・アシャー，Cronicle Asher）\n\n贊斯卡爾帝國女王瑪利亞·阿摩尼亞的弟弟，同時也是贊斯卡爾帝國黃衫軍的菁英機師，與神聖軍事同盟的少年機師胡索·艾溫猶如宿敵一般\n\n駕駛之機體為 ZMT-S34S Rig Contio（利克·岡提奧）")
        self.go_back()

    def on_enter_state0153_menu(self, event):
        print("I'm entering state0153_menu")
        buttons_template = TemplateSendMessage(
            alt_text='贊斯卡爾戰爭主要參戰勢力',
            template=ButtonsTemplate(
                title='贊斯卡爾戰爭主要參戰勢力',
                text='請選擇欲查詢勢力之主角資訊',
                thumbnail_image_url='https://i.imgur.com/Hh59ZNh.jpg',
                actions=[
                    MessageTemplateAction(
                        label='神聖軍事同盟',
                        text='神聖軍事同盟'
                    ),
                    MessageTemplateAction(
                        label='贊斯卡爾帝國',
                        text='贊斯卡爾帝國'
                    ),
                    MessageTemplateAction(
                        label='返回主選單',
                        text='返回'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_page1(self, event):
        print("I'm entering page1_menu")
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
                    MessageTemplateAction(
                        label='到第二頁',
                        text='到第二頁'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_page1_menu(self, event):
        print("I'm entering page1_menu")
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
                    MessageTemplateAction(
                        label='到第二頁',
                        text='到第二頁'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_page2(self, event):
        print("I'm entering page2")
        buttons_template = TemplateSendMessage(
            alt_text='鋼彈歷年戰役資訊查詢',
            template=ButtonsTemplate(
                title='鋼彈歷年戰役資訊查詢',
                text='請選擇欲查詢之宇宙世紀年（Universal Century, U.C）',
                thumbnail_image_url='https://i.imgur.com/O9Nbw2w.jpg',
                actions=[
                    MessageTemplateAction(
                        label='UC.0088',
                        text='0088'
                    ),
                    MessageTemplateAction(
                        label='UC.0093',
                        text='0093'
                    ),
                    MessageTemplateAction(
                        label='UC.0096',
                        text='0096'
                    ),
                    MessageTemplateAction(
                        label='到第三頁',
                        text='到第三頁'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_page2_menu(self, event):
        print("I'm entering page2_menu")
        buttons_template = TemplateSendMessage(
            alt_text='鋼彈歷年戰役資訊查詢',
            template=ButtonsTemplate(
                title='鋼彈歷年戰役資訊查詢',
                text='請選擇欲查詢之宇宙世紀年（Universal Century, U.C）',
                thumbnail_image_url='https://i.imgur.com/O9Nbw2w.jpg',
                actions=[
                    MessageTemplateAction(
                        label='UC.0088',
                        text='0088'
                    ),
                    MessageTemplateAction(
                        label='UC.0093',
                        text='0093'
                    ),
                    MessageTemplateAction(
                        label='UC.0096',
                        text='0096'
                    ),
                    MessageTemplateAction(
                        label='到第三頁',
                        text='到第三頁'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()

    def on_enter_page3(self, event):
        print("I'm entering page3")
        buttons_template = TemplateSendMessage(
            alt_text='鋼彈歷年戰役資訊查詢',
            template=ButtonsTemplate(
                title='鋼彈歷年戰役資訊查詢',
                text='請選擇欲查詢之宇宙世紀年（Universal Century, U.C）',
                thumbnail_image_url='https://i.imgur.com/m4p44jb.jpg',
                actions=[
                    MessageTemplateAction(
                        label='UC.0123',
                        text='0123'
                    ),
                    MessageTemplateAction(
                        label='UC.0133',
                        text='0133'
                    ),
                    MessageTemplateAction(
                        label='UC.0153',
                        text='0153'
                    ),
                    MessageTemplateAction(
                        label='回第一頁',
                        text='回第一頁'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)

    def on_enter_page3_menu(self, event):
        print("I'm entering page3_menu")
        buttons_template = TemplateSendMessage(
            alt_text='鋼彈歷年戰役資訊查詢',
            template=ButtonsTemplate(
                title='鋼彈歷年戰役資訊查詢',
                text='請選擇欲查詢之宇宙世紀年（Universal Century, U.C）',
                thumbnail_image_url='https://i.imgur.com/m4p44jb.jpg',
                actions=[
                    MessageTemplateAction(
                        label='UC.0123',
                        text='0123'
                    ),
                    MessageTemplateAction(
                        label='UC.0133',
                        text='0133'
                    ),
                    MessageTemplateAction(
                        label='UC.0153',
                        text='0153'
                    ),
                    MessageTemplateAction(
                        label='回第一頁',
                        text='回第一頁'
                    ),
                ]
            )
        )
        send_yes_no_button(event.source.user_id, buttons_template)
        self.go_back()