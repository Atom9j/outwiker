��          L      |       �   �  �      C     L     f  $   m  �  �  �       
  )   
     I
  "   ^
                                         Add command (:spoiler:) in wiki parser.

<B>Usage:</B>
<PRE>(:spoiler:)
Text
(:spoilerend:)</PRE>

For nested spoilers use (:spoiler0:), (:spoiler1:)... (:spoiler9:) commands. 

<U>Example:</U>

<PRE>(:spoiler:)
Text
&nbsp;&nbsp;&nbsp;(:spoiler1:)
&nbsp;&nbsp;&nbsp;Nested spoiler
&nbsp;&nbsp;&nbsp;(:spoiler1end:)
(:spoilerend:)</PRE>

<B>Params:</B>
<U>inline</U> - Spoiler will be in inline mode.
<U>expandtext</U> - Link text for the collapsed spoiler. Default: "Expand".
<U>collapsetext</U> - Link text for the expanded spoiler. Default: "Collapse".

<U>Example:</U>

<PRE>(:spoiler expandtext="More..." collapsetext="Less" inline :)
Text
(:spoilerend:)</PRE>
 Collapse Collapse text (:spoiler:) Expand http://jenyay.net/Outwiker/SpoilerEn Project-Id-Version: spoiler
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2014-10-03 21:44+0400
PO-Revision-Date: 2014-10-03 21:45+0300
Last-Translator: Eugeniy Ilin <jenyay.ilin@gmail.com>
Language-Team: Jenyay <jenyay.ilin@gmail.com>
Language: ru_RU
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Poedit-SourceCharset: utf-8
X-Generator: Poedit 1.5.4
 Добавляет вики-команду (:spoiler:) для скрытия части текста на странице (вставка спойлеров).

<B>Использование:</B>
<PRE>(:spoiler:)
Текст
(:spoilerend:)</PRE>

Для вложенных спойлеров используйте команды (:spoiler0:), (:spoiler1:)... (:spoiler9:). 

<U>Пример:</U>

<PRE>(:spoiler:)
Текст
&nbsp;&nbsp;&nbsp;(:spoiler1:)
&nbsp;&nbsp;&nbsp;Вложенный спойлер
&nbsp;&nbsp;&nbsp;(:spoiler1end:)
(:spoilerend:)</PRE>

<B>Параметры:</B>
<U>inline</U> - Спойлер будет оформлен в виде текста без выделения блока.
<U>expandtext</U> - Текст для ссылок, который будет показан, пока спойлер свернут. Значение по умолчанию: "Развернуть".
<U>collapsetext</U> - Текст для ссылок, который будет показан, пока спойлер развернут. Значение по умолчанию: "Свернуть".

<U>Пример:</U>

<PRE>(:spoiler expandtext="Раскукожить" collapsetext="Скукожить" inline:)
Текст
(:spoilerend:)</PRE>
 Свернуть Свёрнутый текст (:spoiler:) Развернуть http://jenyay.net/Outwiker/Spoiler 