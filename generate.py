SEARCH = 0
l = [
      ["/r/", "r", [
          ["/inbox", "i", "https://reddit.com/message/inbox"]
        , ["/modmail", "m", "https://mod.reddit.com/mail/all"]
        , ["/all", "a", "https://reddit.com/r/all"]
        , ["/top", "t", "https://www.reddit.com/r/all/top?sort=top&t=hour"]
        , ["/shithole/","s", [
              ["/default", "d", "https://reddit.com/r/freegamesonsteam"]
            , ["/spam", "s", "https://www.reddit.com/r/FreeGamesOnSteam/about/spam/"]
            , ["/reports", "r", "https://www.reddit.com/r/FreeGamesOnSteam/about/reports/"]
            , ["/new", "n", "https://reddit.com/r/FreeGamesOnSteam/new"]
        ]]
        , ["/common/", "c", [
              ["/seatte", "e","https://reddit.com/r/seattle" ]
            , ["/sysadmin", "s","https://reddit.com/r/sysadmin" ]
            , ["/programmerhumor", "p","https://reddit.com/r/programmerhumor" ]
            , ["/dccomics", "d","https://reddit.com/r/dccomics" ]
            , ["/dumb memes", "a","https://reddit.com/r/anime_irl" ]
            , ["/globaloffensive", "g","https://reddit.com/r/globaloffensive" ]
            , ["/league", "l","https://reddit.com/r/leagueoflegends" ]
            , ["/osu", "o","https://reddit.com/r/osugame" ]
            , ["/tf2", "t","https://reddit.com/r/tf2" ]
        ]]
        , ["/r?", "r", SEARCH, "https://reddit.com/r/%s", "reddit.com/r/"]
        , ["/u?", "u", SEARCH, "https://reddit.com/u/%s", "reddit.com/u/"]
      ]]
    , ["/chan/", "c", [
          ["/ck", "k", "https://4chan.org/ck"]
        , ["/gd", "g", "https://4chan.org/gd"]
        , ["/pro", "p", "https://desuchan.moe/pro/"]
        , ["/tech/", "t", [
              ["/laintech", "l" , "https://lainchan.org/tech/catalog.html"]
            # , ["/desutech", "d", "https://desuchan.moe/tech/"] # dead, one post every three weeks, expired ssl cert
            , ["/g", "g", "https://4chan.org/g"]
            , ["/8", "8", "https://8ch.net/tech/catalog.html"]
            , ["/silicon", "s", "https://sushigirl.us/silicon/catalog.html"]
            , ["/endtech", "e", "https://endchan.xyz/tech/catalog.html"]
            , ["/λ", "p", "https://lainchan.org/%CE%BB/catalog.html"]
            , ["/finaltech", "f", "https://finalchan.net/t/catalog.html"]
            , ["/danger/tech", "d", "https://dangeru.us/tech/"]
        ]]
        , ["/music/", "m", [
              ["/mu", "m", "https://aurorachan.net/mu/"]
            , ["/tunes", "t", "https://sushigirl.us/tunes/catalog.html"]
            , ["/media", "e", "https://uboachan.net/media/catalog.html"]
            , ["/danger/mu", "d", "https://dangeru.us/mu/"]
        ]]
        , ["/transport", "n", "https://boards.4chan.org/n"]
        , ["/news/", "z", [
              ["/4", "4", "https://boards.4chan.org/news"]
            , ["/danger/new", "d", "https://dangeru.us/new/"]
        ]]
        , ["/off_topic/", "o", [
              ["/ot", "o", "https://uboachan.net/ot/catalog.html"]
            , ["/lounge", "l", "https://sushigirl.us/lounge/catalog.html"]
            , ["/danger/u", "d", "https://dangeru.us/u/"]
            , ["/sama", "z", "https://samachan.org/z/catalog.html"]
        ]]
        , ["/lain/", "l" , [
              ["/mega", "m", "https://lainchan.org/mega/catalog.html"]
            , ["/tech", "t", "https://lainchan.org/tech/catalog.html"]
            , ["/lambda", "l", "https://lainchan.org/lambda/catalog.html"]
            , ["/sec", "s", "https://lainchan.org/sec/catalog.html"]
            , ["/mod", "o", "https://lainchan.org/mod.php?/mod/"]
            , ["/reports", "r", "https://lainchan.org/mod.php?/reports"]
        ]]
        , ["/cyb/", "c", [
              #   ["/htll", "h", "https://hightechlowlife.eu/board/"] # down
              ["/chiruno", "c", "https://chiru.no/cyber/"]
            , ["/8", "8", "https://8ch.net/cyber/catalog.html"]
            , ["/final", "f", "https://finalchan.net/1984/"]
            , ["/master", "m", "https://masterchan.org/cyb"]
            , ["/end", "e", "https://endchan.xyz/overboard/"]
            # , ["/penumbranet", "p", "https://penumbra.network/overboard/"] # down
            # , ["/unsafe", "u", "https://jinteki.industries/"] # formerly cyberlife.unsafe.space, down
            , ["/danger/cyb", "d", "https://dangeru.us/cyb/"]
            , ["/danger/lain", "l", "https://dangeru.us/lain/"]
        ]]
        , ["/dynu/", "y", [
              ["/letterbox", "l", "http://afternoon.dynu.com/letterbox.html"]
            , ["/photoboard", "p", "http://afternoon.dynu.com/photo.html"]
        ]]
        , ["/dangeru/", "d", [
              ["/all", "a", "https://dangeru.us/all"]
            , ["/login", "m", "https://dangeru.us/mod"]
            , ["/staff", "s", "https://dangeru.us/staff"]
            , ["/u", "u", "https://dangeru.us/u"]
            , ["/test", "t", "https://dangeru.us/test"]
            , ["/lain", "l", "https://dangeru.us/lain"]
            , ["/tech", "e", "https://dangeru.us/tech"]
            , ["/cyb", "c", "https://dangeru.us/cyb"]
        ]]
        , ["/int/", "i", [
              ["/8/argentina", "a", "https://8ch.net/argentina/catalog.html"]
            , ["/8/canada", "c", "https://8ch.net/canada/catalog.html"]
            , ["/hilo_latino", "h", "https://4chan.org/int"] # TODO
        ]]
      ]]
    , ["/tube/", "t", [
          ["/zero", "0", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KR4Q-pC-7MLb_DoRmzYOCUw"]
        , ["/one", "1", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KRZ43r5UVGNraUgvyPaUMBU"]
        , ["/two", "2", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KQO4aHOqypivLefSFKq2vp1"]
        , ["/three", "3", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KSeW6AmMmg3D4etDs5YeX8q"]
        , ["/four", "4", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KTkhLF_MECKCA8DFWQIsGq7"]
        #, ["/five", "5", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KRlyVVSJZQEt2H-TqU-e_Tf"]
        , ["/favorites", "f", "https://www.youtube.com/playlist?list=FLRkKd3ko9mg_WdWoilM654A"]
        , ["/watchlist", "w", "https://www.youtube.com/playlist?list=WL"]
        , ["/search?", "s", SEARCH, "https://www.youtube.com/results?search_query=%s", "Search Youtube"]
      ]]
    , ["/other/", "o", [
          ["/mebious/", "m", [
              ["/co_uk", "c", "https://mebious.co.uk/"]
            , ["/us", "u", "https://mebio.us/"]
            , ["/neocities", "n", "https://mebious.neocities.org/"]
            , ["/mobi", "m", "https://mebious.mobi/"]
        ]]
        , ["/vola", "v", "https://volafile.io/r/kUFzLJ"]
        , ["/Шрифты", "w", "https://vk.com/topic-50911295_28400542"]
        , ["/scaneye", "s", "https://scaneye.net/"]
        , ["/codewars", "c", "https://codewars.com/dashboard"]
        , ["/files/", "f", [
              ["/filechef", "c", "http://filechef.com"]
            , ["/filepursuit", "p", "https://filepursuit.com"]
            ]]
        , ["/personal/", "p", [
              ["/shmibs", "s", "https://shmibbles.me"]
            , ["/fauux", "f", "https://fauux.neocities.org"]
            , ["/m0nst3rs", "m", "https://m0nst3r.neocities.org/"]
            , ["/ijk", "i", "https://ijk.neocities.org"]
            , ["/ovibos", "o", "https://ovibos.me"]
        ]]
        , ["/books/", "b", [
              ["/ebook-dl", "e", "http://www.wowebook.org/"]
            , ["/it-ebooks", "i", "http://it-ebooks.info/"]
            , ["/bookzz", "z", "https://bookzz.org/"]
            , ["/bookdl", "d", "https://bookdl.com/"]
        ]]
        , ["/nntp", "n", "https://2hu-ch.org/catalog-overchan.technology.html"]
    ]]
    , ["/wikipedia?", "w", SEARCH, "https://en.wikipedia.org/wiki/%s", "Search Wikipedia"]
    , ["/voice", "v", "https://voice.google.com/u/0/messages"]
]
special = "https://niles.xyz"

def rjs(f, z):
    result = []
    result.append("if (" + str(ord(f[1].upper())) + " == x && z == '"+z+"') {")
    result.append("document.getElementById(z+'" + f[1] + "').style.color = '#CC0000';")
    if type(f[2]) == str: # link
        result.append("window.location = '" + f[2] + "';")
    else: # other menu
        result.append("z = z + '"+f[1]+"';")
        result.append("var x = arr(document.getElementsByClassName(z));")
        result.append("x.forEach(function(elem) { elem.style.display = 'inline-block'; })")
        result.append("x[0].parentNode.style.zIndex = 10 * x[0].id.length;")
        result.append("var x = document.getElementById(z);")
        result.append("x.onclick = function() { collapse('" + str(z) + "');}")
    if f[2] == SEARCH: # search box
        result.append("var x = document.getElementById(z + '"+f[1]+"' + 'i');");
        result.append("x.focus();");
        result.append("event.preventDefault();") # this was the magic spice
    result.append("}")
    if type(f[2]) == list:
        for l in f[2]:
            result.append(rjs(l, z + f[1]))
    return "\n".join(result)

def rjs2(f, z):
    result = []
    if type(f[2]) != str: # submenu or search
        result.append("if (z == '"+z+"') {")
        result.append("document.getElementById(z+'" + f[1] + "').onclick = function() { if (z != \""+z+"\") { collapse(\""+z+"\") } key({keyCode:" + str(ord(f[1].upper())) + " }) };")
        result.append("}")
        if type(f[2]) == list: # submenu
            for l in f[2]:
                result.append(rjs2(l, z + f[1]))
    return "\n".join(result)

def rhtml(f, z):
    result = []
    display = ""
    if len(z) > 0:
        display = "style='display: none;'"
    result.append(''.join(["<a class='",z,"' id='",z,f[1],"' ",display," onclick='collapse(\"",z,"\"); key({keyCode:",str(ord(f[1].upper())),"})'>", f[0], "</a>"]))
    if type(f[2]) != str: # submenu or search
        result.append("<span style='position: absolute; left: 200px; top: 0px; width: 300px;'>")
        if type(f[2]) == list: # submenu
            for l in f[2]:
                result.append(rhtml(l, z + f[1]))
        elif f[2] == SEARCH: #  search
            result.append(rsearch(f, z + f[1]))
        result.append("</span>")
    result.append("<br />")
    return "\n".join(result)

def rsearch(f, z):
    result = []
    default = []
    if len(f) > 4:
        default = ["placeholder='", f[4], "'"]
    result.append(''.join(["<form class='"+z+"' id='",z,f[1],"' action='javascript:doSearch(\"",f[3],"\", \"",z,f[1],"\")' style='display: none;'>"]))
    result.append("<input onblur='this.value = \"\";' type='text' name='input' id='"+z+f[1]+"i"+"' " + "".join(default) + " />")
    result.append("</form>")
    return "\n".join(result)


master = ["""<!doctype html>
<!--


This code is auto-generated
Any changes you make will be overwritten when you run "make"

"""]
for i in range(100): master.append("")
master.append("""
-->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link rel="stylesheet" type="text/css" href="style.css">
<script>
var z = "";
var ctrl = false;
var shift = false;
function doSearch(toAddress, inputSelector) {
    var s = document.getElementById(inputSelector + 'i').value;
    //alert(toAddress);
    document.location = toAddress.replace("%s", s);
}
function pi() {
    if (ctrl && shift) {
        window.location = '""" + special + """';
    }
}
function arr(thing) {
    return Array.prototype.slice.call(thing, 0);
}
function collapse_one() {
    var x = arr(document.getElementsByClassName(z));
    x.forEach(function(elem) { elem.style.display = "none"; })
    x[0].parentNode.style.zIndex = 0;
    document.getElementById(z).style.color = '#eeeeee';
    z = z.substring(0, z.length - 1);""")
for f in l:
    master.append(rjs2(f, ""))
master.append("""
}
function collapse(new_z) {
    while(z.length > new_z.length) {
        collapse_one();
    }
}
function keyup(event) {
    event = event || window.event;
    var x = event.which || event.keyCode;
    if (x == 17) {
        ctrl = false;
    }
    if (x == 16) {
        shift = false;
    }

}
function key(event) {
    event = event || window.event;
    if (event.keyCode == 27) {
        if (z.length == 0) {
            return;
        }
        collapse_one()
        return;
    }
    var x = event.which || event.keyCode;
    if (x == 17) {
        ctrl = true;
    }
    if (x == 16) {
        shift = true;
    }
""")
for f in l:
    master.append(rjs(f, ""))
master.append("""
        return true;
}
document.onkeydown = key;
document.onkeyup = keyup;

var ol = function ol() {
    document.getElementById("today").innerHTML = ""; // clear before refreshing
    request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if(request.readyState === 4) {
            if(request.status === 200) {
                var messages = request.responseText.split("\\n");
                var div = document.getElementById("today")
                for (var i = 0; i < messages.length; i++) {
                    if (messages[i].trim().length == 0) continue;
                    var span = document.createElement("span")
                    span.classList.add("message")
	                span.style.marginTop = (5 * i).toString() + "px";
                    span.innerText = messages[i]
                    div.appendChild(span);
                    div.appendChild(document.createElement("br"));
                }
            }
        }
    }
    request.open('GET', 'http://127.0.0.1/today', true);
    request.send(null);
    setTimeout(ol, 60*1000); // refresh every minute
}
</script></head>""")
master.append("""<body class="" onLoad='ol();'><div id="content">""")
for f in l:
    master.append(rhtml(f, ""))
master.append("""</div><div id="today"></div><div id="pi" onclick='pi();'>π</div></body></html>""")
master = "\n".join(master)
print(master)
