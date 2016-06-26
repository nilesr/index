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
        result.append("x.onclick = function() { key({keyCode: 27}) }")
    result.append("}")
    if type(f[2]) != str:
        for l in f[2]:
            result.append(rjs(l, z + f[1]))
    return "\n".join(result)

def rjs2(f, z):
    result = []
    if type(f[2]) != str:
        result.append("if (z == '"+z+"') {")
        result.append("document.getElementById(z+'" + f[1] + "').onclick = function() { key({keyCode:" + str(ord(f[1].upper())) + " }) };")
        result.append("}")
        for l in f[2]:
            result.append(rjs2(l, z + f[1]))
    return "\n".join(result)

def rhtml(f, z):
    result = []
    href = []
    if type(f[2]) == str:
        href = ["href='"+f[2]+"'"]
    if len(z) > 0:
        href = ["style='display: none;'"]
    result.append(''.join(["<a class='"+z+"' id='",z,f[1],"' ",*href," onclick='key({keyCode:"+str(ord(f[1].upper()))+"})'>", f[0], "</a>"]))
    if type(f[2]) != str:
        result.append("<span style='position: absolute; left: 200px; top: 0px;'>")
        for l in f[2]:
            result.append(rhtml(l, z + f[1]))
        result.append("</span>")
    result.append("<br />")
    return "\n".join(result)

l = [
      ["/r/", "r", [
          ["/all", "a", "https://reddit.com/r/all"]
        , ["/top", "t", "https://reddit.com/r/all/top?t=1h"]
        , ["/new", "n", "https://reddit.com/r/FreeGamesOnSteam/new"]
        , ["/shithole","s", "https://reddit.com/r/freegamesonsteam"]
      ]]
    , ["/chan/", "c", [
          ["/ck", "k", "https://4chan.org/ck"]
        , ["/pro", "p", "http://desuchan.moe/pro/"]
        , ["/tech/", "t", [
              ["/laintech", "l" , "https://lainchan.org/tech/catalog.html"]
            , ["/desutech", "d", "http://desuchan.moe/tech/"]
            , ["/g", "g", "https://4chan.org/g"]
            , ["/silicon", "s", "https://sushigirl.us/silicon/catalog.html"]
        ]]
        , ["/music/", "m", [
              ["/mu", "m", "http://aurorachan.net/mu/"]
            , ["/tunes", "t", "https://sushigirl.us/tunes/catalog.html"]
        ]]
        , ["/transport", "n", "http://boards.4chan.org/n"]
        , ["/news", "z", "http://boards.4chan.org/news"]
        , ["/off_topic/", "o", [
              ["/ot", "o", "https://uboachan.net/ot/catalog.html"]
            , ["/lounge", "l", "https://sushigirl.us/lounge/catalog.html"]
        ]]
        , ["/cyb", "c", "https://lainchan.org/cyb/catalog.html"]
        , ["/lit", "l", "https://lainchan.org/lit/catalog.html"]
        , ["/λ", "p", "https://lainchan.org/%CE%BB/catalog.html"]
        , ["/art", "x", "https://lainchan.org/art/catalog.html"]
      ]]
    , ["/vola", "v", "https://volafile.io/r/kUFzLJ"]
    , ["/tube/", "t", [
          ["/0", "0", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KR4Q-pC-7MLb_DoRmzYOCUw"]
        , ["/1", "1", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KRZ43r5UVGNraUgvyPaUMBU"]
        , ["/2", "2", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KQO4aHOqypivLefSFKq2vp1"]
        , ["/3", "3", "https://www.youtube.com/playlist?list=PLIKcw9O7i0KSeW6AmMmg3D4etDs5YeX8q"]
      ]]
    #, ["/mail", "g", "https://gmail.com"] # Fixed tab
]

master = ["""<!doctype html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link rel="stylesheet" type="text/css" href="style.css">
<script>
var z = "";
function key(event) {
    event = event || window.event;
    console.log(event.keyCode);
    if (event.keyCode == 27) {
        if (z.length == 0) {
            return;
        }
        var x = document.getElementsByClassName(z);
        for (var i = 0; i < x.length; i++) { x[i].style.display = 'none'; }
        document.getElementById(z).style.color = '#eeeeee';
        z = z.substring(0, z.length - 1);
        """]
for f in l:
    master.append(rjs2(f, ""))
master.append("""
        return;
    }
    var x = event.which || event.keyCode;
""")
for f in l:
    master.append(rjs(f, ""))
master.append("""
}
document.onkeydown = key;
</script></head>""")
master.append("""<body class="hasGoogleVoiceExt"><div id="content">""")
for f in l:
    master.append(rhtml(f, ""))
master.append("""</div></body></html>""")
master = "\n".join(master)
print(master)
