from abc import ABC, abstractmethod

# Product: ページ
class Page(ABC):
    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_footer(self):
        pass

# Concrete Product 1: HTMLページ
class HtmlPage(Page):
    def create_header(self):
        return "HTML Header"

    def create_body(self):
        return "HTML Body"

    def create_footer(self):
        return "HTML Footer"

# Concrete Product 2: Markdownページ
class MarkdownPage(Page):
    def create_header(self):
        return "Markdown Header"

    def create_body(self):
        return "Markdown Body"

    def create_footer(self):
        return "Markdown Footer"

# Creator: ページを生成するファクトリ
class PageFactory(ABC):
    @abstractmethod
    def create_page(self):
        pass

# Concrete Creator 1: HTMLページのファクトリ
class HtmlPageFactory(PageFactory):
    def create_page(self):
        return HtmlPage()

# Concrete Creator 2: Markdownページのファクトリ
class MarkdownPageFactory(PageFactory):
    def create_page(self):
        return MarkdownPage()

# Client コード
def main():
    html_page_factory = HtmlPageFactory()
    markdown_page_factory = MarkdownPageFactory()

    html_page = html_page_factory.create_page()
    markdown_page = markdown_page_factory.create_page()

    print("HTML Page Components:")
    print(html_page.create_header())
    print(html_page.create_body())
    print(html_page.create_footer())

    print("\nMarkdown Page Components:")
    print(markdown_page.create_header())
    print(markdown_page.create_body())
    print(markdown_page.create_footer())

if __name__ == "__main__":
    main()
