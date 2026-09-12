
## 2. `notes.md`

```markdown
# 📝 Day 016 — Audio, Video and iFrames

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

# 1. HTML Multimedia

Multimedia means content such as:

- Audio
- Video
- Images
- Embedded external content

HTML5 provides built-in elements for working with audio and video.

The main elements are:

- `<audio>`
- `<video>`
- `<source>`
- `<track>`
- `<iframe>`

---

# 2. The `<audio>` Element

The `<audio>` element is used to embed sound or audio files into a webpage.

Basic example:

    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

The `controls` attribute displays the browser's audio controls.

---

# 3. Audio Controls

The browser can provide controls such as:

- Play
- Pause
- Volume
- Progress bar
- Mute

Example:

    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

---

# 4. `autoplay`

The `autoplay` attribute tells the browser to start playing the media automatically.

Example:

    <audio autoplay controls>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

Important:

Modern browsers often restrict autoplay when media has sound.

Therefore, autoplay should be used carefully.

---

# 5. `muted`

The `muted` attribute starts the media without sound.

Example:

    <video controls muted>
        <source src="video.mp4" type="video/mp4">
    </video>

Muted media is commonly used when autoplay is required.

---

# 6. `loop`

The `loop` attribute makes the media start again after it finishes.

Example:

    <audio controls loop>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

---

# 7. `preload`

The `preload` attribute gives the browser a hint about how much media data should be loaded before the user starts playing it.

Common values:

- `none`
- `metadata`
- `auto`

Example:

    <audio controls preload="metadata">
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

`metadata` asks the browser to load basic information such as duration when possible.

---

# 8. The `<source>` Element

The `<source>` element specifies a media file and its MIME type.

Example:

    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
        <source src="audio.ogg" type="audio/ogg">
    </audio>

The browser can choose a supported source.

---

# 9. The `<video>` Element

The `<video>` element is used to embed video content.

Example:

    <video controls width="640">
        <source src="video.mp4" type="video/mp4">
    </video>

The `controls` attribute provides playback controls.

---

# 10. Video Attributes

Common video attributes include:

- `controls`
- `autoplay`
- `muted`
- `loop`
- `preload`
- `width`
- `height`
- `poster`

Example:

    <video
        controls
        width="640"
        height="360"
        poster="thumbnail.jpg">

        <source src="video.mp4" type="video/mp4">

    </video>

---

# 11. `poster`

The `poster` attribute specifies an image that is displayed before the video starts playing.

Example:

    <video
        controls
        poster="thumbnail.jpg">

        <source src="video.mp4" type="video/mp4">

    </video>

The poster works like a preview image for the video.

---

# 12. Audio vs Video

Audio:

    <audio>

Used for sound.

Video:

    <video>

Used for moving visual content, usually with sound.

---

# 13. The `<track>` Element

The `<track>` element provides timed text for media.

It can be used for:

- Subtitles
- Captions
- Descriptions
- Other timed text

Example:

    <video controls>
        <source src="lesson.mp4" type="video/mp4">

        <track
            src="captions.vtt"
            kind="captions"
            srclang="en"
            label="English">

    </video>

The track file is commonly written in WebVTT format.

---

# 14. Why Captions Matter

Captions improve accessibility.

They help:

- Deaf or hard-of-hearing users
- Users watching without sound
- Users learning a language
- Users in noisy or quiet environments

---

# 15. Fallback Content

You can provide fallback text inside audio and video elements.

Example:

    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>

This text can be shown when the browser cannot use the media element.

---

# 16. Local Media Files

A media file can be stored inside the project.

Example structure:

    code/
    │
    ├── index.html
    ├── audio/
    │   └── lesson.mp3
    │
    └── video/
        └── lesson.mp4

Then:

    <audio controls>
        <source src="audio/lesson.mp3" type="audio/mpeg">
    </audio>

And:

    <video controls width="640">
        <source src="video/lesson.mp4" type="video/mp4">
    </video>

---

# 17. What is an `<iframe>`?

An `<iframe>` is an HTML element used to embed another browsing context inside a webpage.

It can be used for content such as:

- Maps
- Videos
- Documents
- Other embeddable webpages
- External widgets

Example:

    <iframe
        src="https://example.com"
        title="Example Website">
    </iframe>

---

# 18. Important iframe Attributes

Common iframe attributes include:

- `src`
- `title`
- `width`
- `height`
- `loading`
- `allow`
- `referrerpolicy`
- `sandbox`

Example:

    <iframe
        src="https://example.com"
        title="Example Content"
        width="600"
        height="400"
        loading="lazy">
    </iframe>

---

# 19. `src`

The `src` attribute specifies the resource that should be embedded.

Example:

    <iframe src="https://example.com"></iframe>

---

# 20. `title`

The `title` attribute provides a description of the iframe content.

Example:

    <iframe
        src="https://example.com"
        title="Example Website">
    </iframe>

A meaningful title is important for accessibility.

---

# 21. `width` and `height`

These attributes define the dimensions of an iframe.

Example:

    <iframe
        src="https://example.com"
        width="600"
        height="400"
        title="Example Website">
    </iframe>

---

# 22. `loading`

The `loading` attribute can control when an iframe is loaded.

Common value:

    loading="lazy"

Lazy loading can help avoid loading off-screen iframe content immediately.

---

# 23. `sandbox`

The `sandbox` attribute can apply restrictions to content loaded inside an iframe.

Example:

    <iframe
        src="https://example.com"
        sandbox
        title="Sandboxed Content">
    </iframe>

A sandbox can restrict certain capabilities of embedded content.

More permissions can be selectively enabled when necessary, but they should not be added without understanding their security implications.

---

# 24. Embedding External Content

Not every website allows itself to be embedded in an iframe.

The external website can use security policies that prevent framing.

Therefore, an iframe may fail even when the URL works normally in a browser tab.

---

# 25. Audio and Video Accessibility

Good multimedia should:

- Provide controls
- Provide captions for videos when appropriate
- Provide meaningful fallback content
- Avoid unexpected autoplay with sound
- Use understandable labels
- Consider users with disabilities

---

# 26. Multimedia File Formats

Common audio formats:

- MP3
- Ogg
- WAV

Common video formats:

- MP4
- WebM
- Ogg

Browser support can vary, so multiple `<source>` elements may sometimes be useful.

---

# 27. Audio Example

Example:

    <audio controls>
        <source src="audio/lesson.mp3" type="audio/mpeg">
        Your browser does not support audio.
    </audio>

---

# 28. Video Example

Example:

    <video controls width="640">
        <source src="video/lesson.mp4" type="video/mp4">
        Your browser does not support video.
    </video>

---

# 29. iFrame Example

Example:

    <iframe
        src="https://example.com"
        title="Example Website"
        width="600"
        height="400"
        loading="lazy">
    </iframe>

---

# 30. Important Difference

`<audio>`:

Used for audio content.

`<video>`:

Used for video content.

`<iframe>`:

Used to embed another browsing context or supported external content.

---

# 31. Best Practices

1. Use `controls` for user-controlled media.
2. Avoid unexpected autoplay with sound.
3. Provide captions when appropriate.
4. Use meaningful iframe titles.
5. Use `loading="lazy"` for suitable off-screen iframes.
6. Use trusted sources for embedded content.
7. Understand iframe security restrictions.
8. Provide fallback content where appropriate.
9. Use suitable media formats.
10. Optimize large media files for webpage performance.

---

# 32. Key Takeaways

- `<audio>` embeds audio.
- `<video>` embeds video.
- `<source>` specifies media sources.
- `<track>` provides timed text such as captions.
- `controls` provides playback controls.
- `autoplay` requests automatic playback.
- `muted` starts media without sound.
- `loop` repeats media.
- `preload` provides a loading hint.
- `poster` provides a video preview image.
- `<iframe>` embeds another browsing context.
- `title` is important for iframe accessibility.
- `sandbox` can restrict iframe capabilities.
- Not every external website permits iframe embedding.