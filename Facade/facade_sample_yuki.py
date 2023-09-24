#このコードは、JavaのFacadeパターンをPythonに変換したものです。
# Facadeパターンは、複雑なシステムに対する単純なインターフェースを提供するデザインパターンです。
# この例では、PageMakerクラスがFacadeとして機能し、
# DatabaseとHtmlWriterクラスの複雑な機能を単純化しています。
# 具体的には、PageMaker.make_welcome_pageメソッドは、
# ユーザー名とメールアドレスを指定するだけでウェルカムページを作成します。
# 内部的には、このメソッドはDatabaseクラスからユーザー情報を取得し、
# HtmlWriterクラスを使用してHTMLファイルを作成します。
#
# しかし、これらの詳細はユーザーから隠蔽されており、
# ユーザーは単純なインターフェースだけを使用します。
# このパターンは、システムが複雑である場合や、システムの一部だけを使用する場合に特に有用です。
# この例では、ウェルカムページの作成が一連の複雑な操作
# （データベースへのアクセス、HTMLファイルの作成など）を必要としますが
# 、Facadeパターンによりこれらが単一のメソッド呼び出しに抽象化されています。

import os
from abc import ABC, abstractmethod

# JavaのインターフェースはPythonの抽象基底クラスに変換します。
class HtmlWriter:
    def __init__(self, writer):
        self.writer = writer

    # タイトルの出力
    def title(self, title):
        self.writer.write("<!DOCTYPE html>\n")
        self.writer.write("<html>\n")
        self.writer.write("<head>\n")
        self.writer.write("<title>" + title + "</title>\n")
        self.writer.write("</head>\n")
        self.writer.write("<body>\n")
        self.writer.write("<h1>" + title + "</h1>\n")

    # 段落の出力
    def paragraph(self, msg):
        self.writer.write("<p>" + msg + "</p>\n")

    # リンクの出力
    def link(self, href, caption):
        self.paragraph("<a href=\"" + href + "\">" + caption + "</a>")

    # メールアドレスの出力
    def mailto(self, mailaddr, username):
        self.link("mailto:" + mailaddr, username)

    # 閉じる
    def close(self):
        self.writer.write("</body>\n")
        self.writer.write("</html>\n")
        self.writer.close()

class Database:
    @staticmethod
    def get_properties(dbname):
        filename = dbname + ".txt"
        prop = {}
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                prop[key] = value
        return prop

class PageMaker:
    @staticmethod
    def make_welcome_page(mailaddr, filename):
        try:
            mailprop = Database.get_properties("maildata")
            username = mailprop[mailaddr]
            with open(filename, 'w') as f:
                writer = HtmlWriter(f)
                writer.title(username + "'s web page")
                writer.paragraph("Welcome to " + username + "'s web page!")
                writer.paragraph("Nice to meet you!")
                writer.mailto(mailaddr, username)
                writer.close()
            print(filename + " is created for " + mailaddr + " (" + username + ")")
        except Exception as e:
            print(str(e))

def main():
    PageMaker.make_welcome_page("hyuki@example.com", "welcome.html")

if __name__ == "__main__":
    main()
