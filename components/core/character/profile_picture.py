"""Profile picture components."""

from modules.element import Element, Component


class ProfilePicture(Component):
    """Definition of profile picture component."""

    profile_pic_border = Element(xpath='//*[@id="characters"]/div/div/div/div[1]/player-image/div[1]')
    add = Element(id_='profilePictureAddToggle')
    done = Element(id_='profilePictureDoneButton')
    default = Element(id_='profilePictureDefaultInput')
    default_image = Element(id_='profilePictureDefaultImageImg')
    image_link = Element(id_='profilePictureImageLinkInput')
    link = Element(id_='profilePictureLinkInput')
    gravatar = Element(id_='profilePictureGravatarInput')
    gravatar_email = Element(id_='profilePictureGravatarEmailInput')
