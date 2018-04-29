"""Footer components."""

from modules import Element, Component


class Footer(Component):
    """Definition of footer component."""

    facebook_id = 'footerFacebookLink'
    twitter_id = 'footerTwitterLink'
    reddit_id = 'footerRedditLink'
    google_plus_id = 'footerGooglePlusLink'
    github_id = 'footerGithubLink'
    rss_id = 'footerRSSLink'
    tiny_letter_id = 'footerTinyLetterLink'
    blog_id = 'footerBlogLink'
    contact_us_id = 'footerContactUsLink'
    patreon_id = 'footerPatreonLink'
    ogl_id = 'footerOGLLink'

    facebook = Element(id_=facebook_id)
    twitter = Element(id_=twitter_id)
    reddit = Element(id_=reddit_id)
    google_plus = Element(id_=google_plus_id)
    github = Element(id_=github_id)
    rss = Element(id_=rss_id)
    tiny_letter = Element(id_=tiny_letter_id)
    blog = Element(id_=blog_id)
    contact_us = Element(id_=contact_us_id)
    patreon = Element(id_=patreon_id)
    ogl = Element(id_=ogl_id)
