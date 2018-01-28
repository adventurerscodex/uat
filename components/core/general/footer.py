"""Footer components."""

from modules.element import Element, Component


class Footer(Component):
    """Definition of footer component."""

    facebook = Element(id_='footerFacebookLink')
    twitter = Element(id_='footerTwitterLink')
    reddit = Element(id_='footerRedditLink')
    google_plus = Element(id_='footerGooglePlusLink')
    github = Element(id_='footerGithubLink')
    rss = Element(id_='footerRSSLink')
    tiny_letter = Element(id_='footerTinyLetterLink')
    blog = Element(id_='footerBlogLink')
    contact_us = Element(id_='footerContactUsLink')
    patreon = Element(id_='footerPatreonLink')
    ogl = Element(id_='footerOGLLink')
