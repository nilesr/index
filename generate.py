l = [
      #["/search?", "s", 0, "https://searx.me/search?q=%s"]
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
            , ["/4chan", "4","https://reddit.com/r/4chan" ]
            , ["/dccomics", "d","https://reddit.com/r/dccomics" ]
            , ["/dumb memes", "a","https://reddit.com/r/anime_irl" ]
            , ["/globaloffensive", "g","https://reddit.com/r/globaloffensive" ]
            , ["/osu", "o","https://reddit.com/r/osugame" ]
            , ["/tf2", "t","https://reddit.com/r/tf2" ]
        ]]
        , ["/r?", "r", 0, "https://reddit.com/r/%s", "reddit.com/r/"]
        , ["/u?", "u", 0, "https://reddit.com/u/%s", "reddit.com/u/"]
      ]]
    , ["/chan/", "c", [
          ["/ck", "k", "https://4chan.org/ck"]
        , ["/gd", "g", "https://4chan.org/gd"]
        , ["/pro", "p", "https://desuchan.moe/pro/"]
        , ["/tech/", "t", [
              ["/laintech", "l" , "https://lainchan.org/tech/catalog.html"]
            , ["/desutech", "d", "https://desuchan.moe/tech/"]
            , ["/g", "g", "https://4chan.org/g"]
            , ["/8", "8", "https://8ch.net/tech/catalog.html"]
            , ["/silicon", "s", "https://sushigirl.us/silicon/catalog.html"]
            , ["/endtech", "e", "https://endchan.xyz/tech/catalog.html"]
            , ["/λ", "p", "https://lainchan.org/%CE%BB/catalog.html"]
            , ["/finaltech", "f", "https://finalchan.net/t/catalog.html"]
        ]]
        , ["/music/", "m", [
              ["/mu", "m", "https://aurorachan.net/mu/"]
            , ["/tunes", "t", "https://sushigirl.us/tunes/catalog.html"]
            , ["/media", "e", "https://uboachan.net/media/catalog.html"]
        ]]
        , ["/transport", "n", "https://boards.4chan.org/n"]
        , ["/news", "z", "https://boards.4chan.org/news"]
        , ["/off_topic/", "o", [
              ["/ot", "o", "https://uboachan.net/ot/catalog.html"]
            , ["/lounge", "l", "https://sushigirl.us/lounge/catalog.html"]
        ]]
        , ["/lain", "l" , "https://lainchan.org/mega/catalog.html"]
        , ["/cyb/", "c", [
              ["/htll", "h", "https://hightechlowlife.eu/board/"]
            , ["/chiruno", "c", "https://chiru.no/cyber/catalog"]
            , ["/8", "8", "https://8ch.net/cyber/catalog.html"]
            , ["/final", "f", "https://finalchan.net/1984/"]
            , ["/master", "m", "https://masterchan.org/cyb"]
            , ["/end", "e", "https://endchan.xyz/overboard/"]
            , ["/penumbranet", "p", "https://penumbra.network/overboard/"]
            , ["/unsafe", "u", "https://jinteki.industries/"] # formerly cyberlife.unsafe.space
        ]]
      ]]
    , ["/tube/", "t", [
          ["/zero", "0", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KR4Q-pC-7MLb_DoRmzYOCUw"]
        , ["/one", "1", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KRZ43r5UVGNraUgvyPaUMBU"]
        , ["/two", "2", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KQO4aHOqypivLefSFKq2vp1"]
        , ["/three", "3", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KSeW6AmMmg3D4etDs5YeX8q"]
        , ["/four", "4", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KTkhLF_MECKCA8DFWQIsGq7"]
        , ["/favorites", "f", "https://www.youtube.com/playlist?list=FLRkKd3ko9mg_WdWoilM654A"]
        , ["/watchlist", "w", "https://www.youtube.com/playlist?list=WL"]
        , ["/search?", "s", 0, "https://www.youtube.com/results?search_query=%s", "Search Youtube"]
      ]]
    , ["/other/", "o", [
          ["/mebious/", "m", [
              ["/co_uk", "c", "https://mebious.co.uk/"]
            , ["/us", "u", "https://mebio.us/"]
            , ["/neocities", "n", "https://mebious.neocities.org/"]
        ]]
        , ["/vola", "v", "https://volafile.io/r/kUFzLJ"]
        , ["/Шрифты", "w", "https://vk.com/topic-50911295_28400542"]
        , ["/scaneye", "s", "https://scaneye.net/"]
        , ["/codewars", "c", "https://codewars.com/dashboard"]
        , ["/filechef", "f", "https://filechef.com"]
        , ["/personal/", "p", [
              ["/shmibs", "s", "https://shmibbles.me"]
            , ["/fauux", "f", "https://fauux.neocities.org"]
            , ["/m0nst3rs", "m", "https://m0nst3r.neocities.org/"]
            , ["/ijk", "i", "https://ijk.neocities.org"]
        ]]
        , ["/books/", "b", [
              ["/ebook-dl", "e", "https://ebook-dl.com/"]
            , ["/it-ebooks", "i", "http://it-ebooks.info/"]
            , ["/bookzz", "z", "https://bookzz.org/"]
        ]]
        , ["/nntp", "n", "https://2hu-ch.org/catalog-overchan.technology.html"]
    ]]
    , ["/wikipedia?", "w", 0, "https://en.wikipedia.org/wiki/%s", "Search Wikipedia"]
]
special = "https://niles.xyz"



def rjs(f, z):
    result = []
    result.append("if (" + str(ord(f[1].upper())) + " == x && z == '"+z+"') {")
    result.append("document.getElementById(z+'" + f[1] + "').style.color = '#CC0000';")
    if type(f[2]) == str:
        result.append("window.location = '" + f[2] + "';")
    else:
        result.append("z = z + '"+f[1]+"';")
        result.append("var x = document.getElementsByClassName(z);")
        result.append("for (var i = 0; i < x.length; i++) { x[i].style.display = 'inline-block'; }")
        result.append("var x = document.getElementById(z);")
        result.append("x.onclick = function() { collapse('" + str(z) + "');}")
    if f[2] == 0:
        result.append("var x = document.getElementById(z + '"+f[1]+"' + 'i');");
        # result.append("x.value = '';")
        result.append("x.focus();");
        # result.append("var x = document.getElementById(z + '"+f[1]+"');");
        # result.append("x.innerHTML = '';")
        # result.append("var tempform = document.createElement('form');");
        # result.append("var tempinput = document.createElement('input');")
        # result.append("tempform.appendChild(tempinput); x.appendChild(tempform);")
        # result.append("tempinput.focus();")
        # result.append("tempinput.value = '';")
        result.append("event.preventDefault();") # this was the magic spice
    result.append("}")
    if type(f[2]) == list:
        for l in f[2]:
            result.append(rjs(l, z + f[1]))
    return "\n".join(result)

def rjs2(f, z):
    result = []
    if type(f[2]) != str:
        result.append("if (z == '"+z+"') {")
        result.append("document.getElementById(z+'" + f[1] + "').onclick = function() { if (z != \""+z+"\") { collapse(\""+z+"\") } key({keyCode:" + str(ord(f[1].upper())) + " }) };")
        result.append("}")
        if type(f[2]) == list:
            for l in f[2]:
                result.append(rjs2(l, z + f[1]))
        elif f[2] == 0:
            #result.append("document.getElementById(z + '"+ f[1] +"' + 'i').value = ''")
            # replaced with the onBlur thing
            pass
    return "\n".join(result)

def rhtml(f, z):
    result = []
    href = ""
    # no longer needed because the onclick handler redirects the page
    # if type(f[2]) == str:
        # href = "href='"+f[2]+"'"
    if len(z) > 0:
        href = "style='display: none;'"
    result.append(''.join(["<a class='"+z+"' id='",z,f[1],"' ",href," onclick='collapse(\""+z+"\"); key({keyCode:"+str(ord(f[1].upper()))+"})'>", f[0], "</a>"]))
    if type(f[2]) != str:
        result.append("<span style='position: absolute; left: 200px; top: 0px; width: 300px;'>")
        if type(f[2]) == list:
            for l in f[2]:
                result.append(rhtml(l, z + f[1]))
        elif f[2] == 0:
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
function collapse_one() {
    var x = document.getElementsByClassName(z);
    for (var i = 0; i < x.length; i++) { x[i].style.display = 'none'; }
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
        """)
master.append("""
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
</script></head>""")
master.append("""<body class=""><div id="content">""")
for f in l:
    master.append(rhtml(f, ""))
master.append("""</div><div id="pi" onclick='pi();'>π</div></body></html>""")
master = "\n".join(master)
print(master)
