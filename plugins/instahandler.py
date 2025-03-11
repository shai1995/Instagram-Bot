if message.text.startswith("/insta"):
    # Instagram URL को प्राप्त करें
    insta_url = message.text.replace("/insta", "").strip()
    
    # API URL तैयार करें
    api_url = f"https://insta-dl.hazex.workers.dev/?url={insta_url}"
    response = HTTP.get(api_url)
    
    # यदि अनुरोध सफल है
    if response.status_code == 200:
        data = bunchify(response.json())
        
        download_url = data.result.url
        extension = data.result.extension
        
        # चैनल के लिए इनलाइन बटन
        inline_button = {
            "inline_keyboard": [[
                {"text": "🔗 Join Our Channel", "url": "https://t.me/BOTxUPDATE"}
            ]]
        }
        
        # मीडिया के प्रकार के आधार पर भेजें
        if extension in ["mp4", "mkv"]:
            bot.sendChatAction(chat_id=message.chat.id, action="upload_video")
            bot.sendVideo(
                chat_id=message.chat.id,
                video=download_url,
                caption="🎥 *Instagram Video*",
                parse_mode="markdown",
                reply_to_message_id=message.message_id,
                reply_markup=inline_button
            )
        elif extension in ["jpg", "jpeg", "png"]:
            bot.sendChatAction(chat_id=message.chat.id, action="upload_photo")
            bot.sendPhoto(
                chat_id=message.chat.id,
                photo=download_url,
                caption="📸 *Instagram Photo*",
                parse_mode="markdown",
                reply_to_message_id=message.message_id,
                reply_markup=inline_button
            )
        else:
            # असमर्थित मीडिया प्रारूप के लिए जवाब
            bot.replyText(
                chat_id=message.chat.id, 
                text="⚠️ *Unsupported media format.*", 
                reply_to_message_id=message.message_id
            )
    else:
        # URL को प्रोसेस करने में त्रुटि
        bot.replyText(
            chat_id=message.chat.id,
            text="⚠️ *Oops! Unable to process the URL. Please check the link and try again.*", 
            reply_to_message_id=message.message_id
        )
