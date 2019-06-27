from urllib import request, error


if __name__ == '__main__':

    url = 'http://www.renren.com/971280070/newsfeed/photo'
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()

        with open("rsp_rrw.html", "w") as f:
            f.write(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)