"""Profile picture components."""

from component_objects import Element, Component


class ProfilePicture(Component):
    """Definition of profile picture component."""

    profile_pic_border_xpath = '//*[@id="characters"]/div/div/div/div[1]/player-image/div[1]'
    add_id = 'profilePictureAddToggle'
    done_id = 'profilePictureDoneButton'
    default_id = 'profilePictureDefaultInput'
    default_image_id = 'profilePictureDefaultImageImg'
    image_link_id = 'profilePictureImageLinkInput'
    link_id = 'profilePictureLinkInput'
    gravatar_id = 'profilePictureGravatarInput'
    gravatar_email_id = 'profilePictureGravatarEmailInput'

    profile_pic_border = Element(xpath=profile_pic_border_xpath)
    add = Element(id_=add_id)
    done = Element(id_=done_id)
    default = Element(id_=default_id)
    default_image = Element(id_=default_image_id)
    image_link = Element(id_=image_link_id)
    link = Element(id_=link_id)
    gravatar = Element(id_=gravatar_id)
    gravatar_email = Element(id_=gravatar_email_id)
