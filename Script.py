class script(object):
    START_TXT = """š·š“š»š¾ {},
š¼š š½š°š¼š“ šøš <a href=https://t.me/{}>{}</a>, \nšāš° šØš šØš šŗšššš šØšššššššššššš š»ššššššš š©šš š»š š·šššššš š“ššššš š°š š»ššššššš š®ššššš...

 šš±ššš šØšš š“š š»š šššš š®šššš šššš šØšššš š¹ššššš šØšš šŗšš š“š š“šššš..š"""

    HELP_TXT = """š·š“š {}
š·š“šš“ šøš š¼š š·š“š»šæ š²š¾š¼š¼š°š½š³š.

šš»āāļø š³ššššššŗš š¦ššš½š¾ @RhythmRockerz

ā š ššŗšššŗš»šš¾ š¢ššššŗšš½š
     
 /alive - Check I'm Alive..
 /status - Bot Status
 /info - User info
 /ping - To get your ping
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (š®ššš¾š š®ššš)

ā <u>š­šššš¼š¾</u> š:-

š£ššš š²ššŗš š¬š¾...š¤

š šÆššš¾šš¾š½ š»š <a href=https://t.me/RyanRR_Bot>ā Ę¦ Ī³ Ī± Šø ā</a>"""

    ABOUT_TXT = """ā­āāāā[ šššØš®š­ ššš” ]āāāāā
ā
āā š“šš šµššš : {}
ā
āā š¶šššš : <a href=https://t.me/RyanRR_Bot>ā Ę¦ Ī³ Ī± Šø ā</a>
ā
āā š½šššššš : š·.šø.š¶ [ šµšš”š ]
ā
āā šŗššššš : ššš
ā
āā š³ššššššš : šš¦š”ššš š¹.š·š¶.š»
ā
āā š­šššššššš : šš¦šššššš š·.šŗ.š·š¼
ā
āā š«šššššššš    : <a href=https://t.me/RyanRR_Bot>ā Ę¦ Ī³ Ī± Šø ā</a>
ā
āā š·šššššš š©š :  <a href=https://t.me/RhythmRockerz>šššš š š</a>
ā
ā°āāāā[<a href=https://t.me/RhythmRockerz>š½š±šš½š±š¶ āšøš¬š“š®š»š</a>]āāāāā"""

    SOURCE_TXT = """<b>NOTE:</b>
Special Thanks to LUCIFER for the codes 
<b>DEV:</b>

- <a href=https://t.me/rithesh_rkrm_17>ćį“ÉŖŹį“ć</a>

- Source - https://github.com/ritheshrkrm/PiroAutoFilterBot""" #please don't change repo link give credit :)

    MANUELFILTER_TXT = """Źį“Źį“: <b>ź°ÉŖŹį“į“Źź±</b>
- ź°ÉŖŹį“į“Ź ÉŖź± į“ ź°į“į“į“į“Źį“ į“”į“Źį“ į“ź±į“Źź± į“į“É“ ź±į“į“ į“į“į“į“į“į“į“į“į“ Źį“į“ŹÉŖį“ź± ź°į“Ź į“ į“į“Źį“ÉŖį“į“Źį“Ź į“į“Źį“”į“Źį“ į“É“į“ ÉŖ į“”ÉŖŹŹ Źį“ź±į“į“É“į“ į“”Źį“É“į“į“ į“Ź į“ į“į“Źį“”į“Źį“ ÉŖź± ź°į“į“É“į“ ÉŖÉ“ į“Źį“ į“į“ź±ź±į“É¢į“
<b>É“į“į“į“:</b>
1. į“ŹÉŖź± Źį“į“ ź±Źį“į“Źį“ Źį“į“ į“ į“į“į“ÉŖÉ“ į“ŹÉŖį“ ÉŖŹį“É¢į“.
2. į“É“ŹŹ į“į“į“ÉŖÉ“ź± į“į“É“ į“į“į“ ź°ÉŖŹį“į“Źź± ÉŖÉ“ į“ į“Źį“į“.
3. į“Źį“Źį“ Źį“į“į“į“É“ź± Źį“į“ į“ į“ ŹÉŖį“ÉŖį“ į“ź° 64 į“Źį“Źį“į“į“į“Źź±.

Cį“į“į“į“É“į“s AÉ“į“ Usį“É¢į“:

ā¢ /filter - <code>į“į“į“ į“ ź°ÉŖŹį“į“Ź ÉŖÉ“ į“ į“Źį“į“</code>
ā¢ /filters - <code>ŹÉŖź±į“ į“ŹŹ į“Źį“ ź°ÉŖŹį“į“Źź± į“ź° į“ į“Źį“į“</code>
ā¢ /del - <code>į“į“Źį“į“į“ į“ ź±į“į“į“ÉŖź°ÉŖį“ ź°ÉŖŹį“į“Ź ÉŖÉ“ į“ į“Źį“į“</code>
ā¢ /delall - <code>į“į“Źį“į“į“ į“Źį“ į“”Źį“Źį“ ź°ÉŖŹį“į“Źź± ÉŖÉ“ į“ į“Źį“į“ (į“Źį“į“ į“į“”É“į“Ź į“É“ŹŹ)</code>"""

    BUTTON_TXT = """Źį“Źį“: <b>Źį“į“į“į“É“ź±</b>
- į“ŹÉŖź± Źį“į“ ź±į“į“į“į“Źį“ź± Źį“į“Ź į“ŹŹ į“É“į“ į“Źį“Źį“ ÉŖÉ“ŹÉŖÉ“į“ Źį“į“į“į“É“ź±.
<b>É“į“į“į“:</b>
1. į“į“Źį“É¢Źį“į“ į“”ÉŖŹŹ É“į“į“ į“ŹŹį“į“”ź± Źį“į“ į“į“ ź±į“É“į“ Źį“į“į“į“É“ź± į“”ÉŖį“Źį“į“į“ į“É“Ź į“į“É“į“į“É“į“, ź±į“ į“į“É“į“į“É“į“ ÉŖź± į“į“É“į“į“į“į“ŹŹ.
2. į“ŹÉŖź± Źį“į“ ź±į“į“į“į“Źį“ź± Źį“į“į“į“É“ź± į“”ÉŖį“Ź į“É“Ź į“į“Źį“É¢Źį“į“ į“į“į“ÉŖį“ į“Źį“į“.
3. Źį“į“į“į“É“ź± ź±Źį“į“Źį“ Źį“ į“Źį“į“į“ŹŹŹ į“į“Źź±į“į“ į“ź± į“į“Źį“į“į“į“”É“ ź°į“Źį“į“į“
<b>į“ŹŹ Źį“į“į“į“É“ź±:</b>
<code>[Button Text](buttonurl:https://t.me/rai_info17)</code>
<b>į“Źį“Źį“ Źį“į“į“į“É“ź±:</b>
<code>[Button Text](buttonalert:į“ŹÉŖź± ÉŖź± į“É“ į“Źį“Źį“ į“į“ź±ź±į“É¢į“)</code>"""

    AUTOFILTER_TXT = """Źį“Źį“: <b>į“į“į“į“ ź°ÉŖŹį“į“Ź</b>
<b>É“į“į“į“: FÉŖŹį“ IÉ“į“į“x</b>
1. į“į“į“į“ į“į“ į“Źį“ į“į“į“ÉŖÉ“ į“ź° Źį“į“Ź į“Źį“É“É“į“Ź ÉŖź° ÉŖį“'ź± į“ŹÉŖį“ į“į“į“.
2. į“į“į“į“ ź±į“Źį“ į“Źį“į“ Źį“į“Ź į“Źį“É“É“į“Ź į“į“į“ź± É“į“į“ į“į“É“į“į“ÉŖÉ“ź± į“į“į“ŹÉŖį“ź±, į“į“ŹÉ“ į“É“į“ ź°į“į“į“ ź°ÉŖŹį“ź±.
3. ź°į“Źį“”į“Źį“ į“Źį“ Źį“ź±į“ į“į“ź±ź±į“É¢į“ į“į“ į“į“ į“”ÉŖį“Ź Qį“į“į“į“ź±. ÉŖ'ŹŹ į“į“į“ į“ŹŹ į“Źį“ ź°ÉŖŹį“ź± ÉŖÉ“ į“Źį“į“ į“Źį“É“É“į“Ź į“į“ į“Ź į“Ź.

<b>Nį“į“į“: Aį“į“į“FÉŖŹį“į“Ź</b>
1. Aį“į“ į“Źį“ Źį“į“ į“s į“į“į“ÉŖÉ“ į“É“ Źį“į“Ź É¢Źį“į“į“.
2. Usį“ /connect į“É“į“ į“į“É“É“į“į“į“ Źį“į“Ź É¢Źį“į“į“ į“į“ į“Źį“ Źį“į“.
3. Usį“ /settings į“É“ Źį“į“'s PM į“É“į“ į“į“ŹÉ“ į“É“ Aį“į“į“FÉŖŹį“į“Ź į“É“ į“Źį“ sį“į“į“ÉŖÉ“É¢s į“į“É“į“."""

    CONNECTION_TXT = """Źį“Źį“: <b>į“į“É“É“į“į“į“ÉŖį“É“ź±</b>
- į“ź±į“į“ į“į“ į“į“É“É“į“į“į“ Źį“į“ į“į“ į“į“ ź°į“Ź į“į“É“į“É¢ÉŖÉ“É¢ ź°ÉŖŹį“į“Źź± 
- ÉŖį“ Źį“Źį“ź± į“į“ į“į“ į“ÉŖį“ ź±į“į“į“į“ÉŖÉ“É¢ ÉŖÉ“ É¢Źį“į“į“ź±.
<b>É“į“į“į“:</b>
1. į“É“ŹŹ į“į“į“ÉŖÉ“ź± į“į“É“ į“į“į“ į“ į“į“É“É“į“į“į“ÉŖį“É“.
2. ź±į“É“į“ <code>/į“į“É“É“į“į“į“</code> ź°į“Ź į“į“É“É“į“į“į“ÉŖÉ“É¢ į“į“ į“į“ Źį“į“Ź į“į“
Cį“į“į“į“É“į“s AÉ“į“ Usį“É¢į“:
ā¢ /connect  - <code>į“į“É“É“į“į“į“ į“ į“į“Źį“ÉŖį“į“Źį“Ź į“Źį“į“ į“į“ Źį“į“Ź į“į“</code>
ā¢ /disconnect  - <code>į“ÉŖź±į“į“É“É“į“į“į“ ź°Źį“į“ į“ į“Źį“į“</code>
ā¢ /connections - <code>ŹÉŖź±į“ į“ŹŹ Źį“į“Ź į“į“É“É“į“į“į“ÉŖį“É“ź±</code>"""

    EXTRAMOD_TXT = """Źį“Źį“: Exį“Źį“ Mį“į“į“Źį“s
<b>É“į“į“į“:</b>
į“Źį“ź±į“ į“Źį“ į“Źį“ į“xį“Źį“ ź°į“į“į“į“Źį“ź± į“ź° į“ŹÉŖź± Źį“į“
Cį“į“į“į“É“į“s AÉ“į“ Usį“É¢į“:
ā¢ /id - <code>É¢į“į“ ÉŖį“ į“ź° į“ ź±į“į“į“ÉŖź°ÉŖį“į“ į“ź±į“Ź.</code>
ā¢ /info  - <code>É¢į“į“ ÉŖÉ“ź°į“Źį“į“į“ÉŖį“É“ į“Źį“į“į“ į“ į“ź±į“Ź.</code>
ā¢ /imdb  - <code>É¢į“į“ į“Źį“ ź°ÉŖŹį“ ÉŖÉ“ź°į“Źį“į“į“ÉŖį“É“ ź°Źį“į“ ÉŖį“į“Ź ź±į“į“Źį“į“.</code>
ā¢ /search  - <code>É¢į“į“ į“Źį“ ź°ÉŖŹį“ ÉŖÉ“ź°į“Źį“į“į“ÉŖį“É“ ź°Źį“į“ į“ į“ŹÉŖį“į“ź± ź±į“į“Źį“į“ź±.</code>"""

    ADMIN_TXT = """Źį“Źį“: Aį“į“ÉŖÉ“ Mį“į“s
<b>É“į“į“į“:</b>
TŹÉŖs Mį“į“į“Źį“ OÉ“ŹŹ Wį“Źį“s Fį“Ź MŹ Aį“į“ÉŖÉ“s
Cį“į“į“į“É“į“s AÉ“į“ Usį“É¢į“:
ā¢ /logs - <code>į“į“ É¢į“į“ į“Źį“ Źį“į“į“É“į“ į“ŹŹį“Źź±</code>
ā¢ /stats - <code>į“į“ É¢į“į“ ź±į“į“į“į“ź± į“ź° ź°ÉŖŹį“ź± ÉŖÉ“ į“Ź. [TŹÉŖs Cį“į“į“į“É“į“ Cį“É“ Bį“ Usį“į“ BŹ AÉ“Źį“É“į“]</code>
ā¢ /delete - <code>į“į“ į“į“Źį“į“į“ į“ ź±į“į“į“ÉŖź°ÉŖį“ ź°ÉŖŹį“ ź°Źį“į“ į“Ź.</code>
ā¢ /users - <code>į“į“ É¢į“į“ ŹÉŖź±į“ į“ź° į“Ź į“ź±į“Źź± į“É“į“ ÉŖį“ź±.</code>
ā¢ /chats - <code>į“į“ É¢į“į“ ŹÉŖź±į“ į“ź° į“Ź į“Źį“į“ź± į“É“į“ ÉŖį“ź±</code>
ā¢ /leave  - <code>į“į“ Źį“į“į“ į“ ź°Źį“į“ į“ į“Źį“į“.</code>
ā¢ /disable  -  <code>į“į“ į“ÉŖź±į“ŹŹį“ į“ į“Źį“į“.</code>
ā¢ /ban  - <code>į“į“ Źį“É“ į“ į“ź±į“Ź.</code>
ā¢ /unban  - <code>į“į“ į“É“Źį“É“ į“ į“ź±į“Ź.</code>
ā¢ /channel - <code>į“į“ É¢į“į“ ŹÉŖź±į“ į“ź° į“į“į“į“Ź į“į“É“É“į“į“į“į“į“ į“Źį“É“É“į“Źź±</code>
ā¢ /broadcast - <code>į“į“ ŹŹį“į“į“į“į“ź±į“ į“ į“į“ź±ź±į“É¢į“ į“į“ į“ŹŹ į“ź±į“Źź±</code>
ā¢ /group_broadcast - <code>Tį“ ŹŹį“į“į“į“į“sį“ į“ į“į“ssį“É¢į“ į“į“ į“ŹŹ į“į“É“É“į“į“į“į“į“ É¢Źį“į“į“s.</code>
ā¢ /gfilter - <code>į“į“ į“į“į“ É¢Źį“Źį“Ź ŅÉŖŹį“į“Źs</code>
ā¢ /gfilters - <code>į“į“ į“ ÉŖį“į“” ŹÉŖsį“ į“Ņ į“ŹŹ É¢Źį“Źį“Ź ŅÉŖŹį“į“Źs</code>
ā¢ /delg - <code>į“į“ į“į“Źį“į“į“ į“ sį“į“į“ÉŖŅÉŖį“ É¢Źį“Źį“Ź ŅÉŖŹį“į“Ź</code>
ā¢ /request - <code>Tį“ sį“É“į“ į“ Mį“į“ ÉŖį“/Sį“ŹÉŖį“s Źį“į“ĢØį“į“sį“ į“į“ Źį“į“ į“į“į“ÉŖÉ“s. OÉ“ŹŹ į“”į“Źį“s į“É“ sį“į“į“į“Źį“ É¢Źį“į“į“. [TŹÉŖs Cį“į“į“į“É“į“ Cį“É“ Bį“ Usį“į“ BŹ AÉ“Źį“É“į“]</code>
ā¢ /delallg - <code>Tį“ į“į“Źį“į“į“ į“ŹŹ GŅÉŖŹį“į“Źs ŅŹį“į“ į“Źį“ Źį“į“'s į“į“į“į“Źį“sį“.</code>
ā¢ /deletefiles - <code>Tį“ į“į“Źį“į“į“ Cį“į“RÉŖį“ į“É“į“ PŹį“DVD FÉŖŹį“s ŅŹį“į“ į“Źį“ Źį“į“'s į“į“į“į“Źį“sį“.</code>"""

    STATUS_TXT = """ā­āāāā[ šŗššššššššš ]āāāāā
ā
āā š»šššš š­šššš : <code>{}</code>
āā š»šššš š¼šššš : <code>{}</code>
āā š»šššš šŖšššš : <code>{}</code>
āā š¼ššš šŗšššššš : <code>{}</code> MiB
āā š­ššš šŗšššššš : <code>{}</code> MiB
ā
ā°āāāā[ š¹ššššš š¹šššššš ]āāāāā """

    LOG_TEXT_G = """#NewGroup
GŹį“į“į“ = {}(<code>{}</code>)
Tį“į“į“Ź Mį“į“Źį“Źs = <code>{}</code>
Aį“į“į“į“ BŹ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nį“į“į“ - {}"""

    ALRT_TXT = """Hello {},
This is Not your Request
Request Yourself..."""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CUDNT_FND = """<b><i>
šØ š¼šššš½š'š šæššš½ šŗššššššš šš¾ššŗšš¾š½ šš šššŗš
š£šš½ ššš šš¾šŗš šŗšš ššš¾ ššæ ššš¾šš¾?</i></b>"""

    I_CUDNT = """ā <b>šØ š¼šššš½š'š šæššš½ šŗššššššš šš¾ššŗšš¾š½ šš šššŗš</b>\n\nā¼ <b><i>š±š¾šššš šš šŗš½ššš ā¶ @RyanRR_Bot</i></b>"""

    I_CUD_NT = """ā <b>šØ š¼šššš½š'š šæššš½ šŗššššššš šš¾ššŗšš¾š½ šš šššŗš</b>\n\nā¼ <b><i>š±š¾šššš šš šŗš½ššš ā¶ @RyanRR_Bot</i></b>"""

    MVE_NT_FND = """ā <b>šØ š¼šššš½š'š šæššš½ šŗššššššš šš¾ššŗšš¾š½ šš šššŗš</b>\n\nā¼ <b><i>š±š¾šššš šš šŗš½ššš ā¶ @RyanRR_Bot</i></b>"""

    TOP_ALRT_MSG = """š¢šš¾š¼šššš šæšš ššš¾šš šš š£šŗššŗš»šŗšš¾..."""

    MELCOW_ENG = """<b>Hey {}, Welcome to {}</b> 

ā¢ š­š šÆšššš, š­š šÆššš, š­š š®ššš¾š š š»ššš¾š
ā¢ š šš šøššš š¬šššš¾š š¶ššš š¢šššš¾š¼š š²šš¾ššššš
ā¢ š²ššŗššš¾šš š²ššŗš š ššŗš
ā¢ š„š¾š¾š š„šš¾š¾ š³š š±š¾šššš š šš š¤ššššš š³š š š½šššš ššššš @admin

<u>š„š²š¾šš²ššš šš¼šæšŗš®šš</u>

ā Petta 2019
ā Mr & Mrs arjun 2021
ā Gatta Kusthi 2022
ā Padayappa 1999
ā 7aum Arivu 2011

ā¼ļøšš¼š»š š®š±š± šš¼šæš±š & šššŗšÆš¼š¹š š¹š¶šøš² , . -  send link movie series š²šš°ā¼ļø"""

    OWNER_INFO = """
ā š¢šš¾šŗššš : <a href='https://t.me/RyanRR_Bot'>š³ššš šÆš¾šššš</a>
"""

    NORSLTS = """
#NoResults 

ID <b>: {}</b>

Name <b>: {}</b>

Message <b>: {}</b>"""

    CAPTION = """
<b>ā­āā[š¹š¹_šššø]āāāā§</b> 
<b>ā</b> 
<b>āā š š¹ššš šµššš : <code>Ā«ā”šš·ššš·š¼šš¾š²šŗš“ššā¢ā”Ā»{file_name}</code>  </b> 
<b>ā</b> 
<b>āāšš¹ššš šŗššš : <code>{file_size}</code> </b> 
<b>ā</b> 
<b>ā°āā[š¹ššššš š¹šššššš]āāā</b>"""

    IMDB_TEMPLATE_TXT = """
<b>š ššøšš»š“</b>: <a href={url}>{title}</a>
<b>š­ š¶š“š½šš“š</b>: {genres}
<b>š šš“š°š</b>: <a href={url}/releaseinfo>{year}</a>
<b>š šš°ššøš½š¶</b>: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
<b>š š»š°š½š¶šš°š¶š“</b>: <code>{languages}</code>
<b>š ššš½š½šøš½š¶ ššøš¼š“</b>: {runtime} Minutes
<b>š šš“š»š“š°šš“ šøš½šµš¾</b>: {release_date}
<b>š š²š¾šš½šššøš“š</b>: <code>{countries}</code>
ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢
šŹį“Ļį“į“sį“į“į“ ŹŹ : {message.from_user.mention}

šį“į“į“”į“Źį“į“ ŹŹ : @RhythmRockerz
ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢ā¢
<b>āÉ“į“į“į“ : ą®ą®¤ą®æą®²ąÆ ą®µą®°ąÆą®®ąÆ ą®ą®©ąÆą®¤ąÆą®¤ąÆą®®ąÆ ą®¤ą®®ą®æą®“ąÆ ą®®ą®ąÆą®ąÆą®®ąÆš</b>"""
    
    ALL_FILTERS = """
<b>Hį“Ź {}, TŹį“sį“ į“Źį“ į“Ź į“ŹŹį“į“ į“Źį“į“s į“Ņ ŅÉŖŹį“į“Źs.</b>"""
    
    GFILTER_TXT = """
<b>Wį“Źį“į“į“į“ į“į“ GŹį“Źį“Ź FÉŖŹį“į“Źs. GŹį“Źį“Ź FÉŖŹį“į“Źs į“Źį“ į“Źį“ ŅÉŖŹį“į“Źs sį“į“ ŹŹ Źį“į“ į“į“į“ÉŖÉ“s į“”ŹÉŖį“Ź į“”ÉŖŹŹ į“”į“Źį“ į“É“ į“ŹŹ É¢Źį“į“į“s.</b>
    
Aį“ į“ÉŖŹį“ŹŹį“ į“į“į“į“į“É“į“s:
ā¢ /gfilter - <code>Tį“ į“Źį“į“į“į“ į“ É¢Źį“Źį“Ź ŅÉŖŹį“į“Ź.</code>
ā¢ /gfilters - <code>Tį“ į“ ÉŖį“į“” į“ŹŹ É¢Źį“Źį“Ź ŅÉŖŹį“į“Źs.</code>
ā¢ /delg - <code>Tį“ į“į“Źį“į“į“ į“ į“į“Źį“ÉŖį“į“Źį“Ź É¢Źį“Źį“Ź ŅÉŖŹį“į“Ź.</code>
ā¢ /delallg - <code>į“į“ į“į“Źį“į“į“ į“ŹŹ É¢Źį“Źį“Ź ź°ÉŖŹį“į“Źź±.</code>"""
    
    FILE_STORE_TXT = """
<b>FÉŖŹį“ sį“į“Źį“ ÉŖs į“Źį“ Ņį“į“į“į“Źį“ į“”ŹÉŖį“Ź į“”ÉŖŹŹ į“Źį“į“į“į“ į“ sŹį“Źį“į“ŹŹį“ ŹÉŖÉ“į“ į“Ņ į“ sÉŖÉ“É¢Źį“ į“Ź į“į“Źį“ÉŖį“Źį“ ŅÉŖŹį“s.</b>

Aį“ į“ÉŖŹį“ŹŹį“ į“į“į“į“į“É“į“s:
ā¢ /batch - <code>Tį“ į“Źį“į“į“į“ į“ Źį“į“į“Ź ŹÉŖÉ“į“ į“Ņ į“į“Źį“ÉŖį“Źį“ ŅÉŖŹį“s.</code>
ā¢ /link - <code>Tį“ į“Źį“į“į“į“ į“ sÉŖÉ“É¢Źį“ ŅÉŖŹį“ sį“į“Źį“ ŹÉŖÉ“į“.</code>
ā¢ /pbatch - <code>Jį“sį“ ŹÉŖį“į“ /batch, Źį“į“ į“Źį“ ŅÉŖŹį“s į“”ÉŖŹŹ Źį“ sį“É“į“ į“”ÉŖį“Ź Ņį“Źį“”į“Źį“ Źį“sį“ŹÉŖį“į“ÉŖį“É“s.</code>
ā¢ /plink - <code>Jį“sį“ ŹÉŖį“į“ /link, Źį“į“ į“Źį“ ŅÉŖŹį“ į“”ÉŖŹŹ Źį“ sį“É“į“ į“”ÉŖį“Ź Ņį“Źį“”į“Źį“ Źį“sį“ŹÉŖį“į“ÉŖį“É“.</code>"""

    RESTART_TXT = """
<b>Bį“į“ Rį“sį“į“Źį“į“į“ !

š Dį“į“į“ : <code>{}</code>
ā° TÉŖį“į“ : <code>{}</code>
š TÉŖį“į“į“¢į“É“į“ : <code>Asia/Kolkata</code>
š ļø Bį“ÉŖŹį“ Sį“į“į“į“s: <code>v2.7.1 [ Sį“į“ŹŹį“ ]</code></b>"""

    LOGO = """ RHYTHM ROCKERZ """
