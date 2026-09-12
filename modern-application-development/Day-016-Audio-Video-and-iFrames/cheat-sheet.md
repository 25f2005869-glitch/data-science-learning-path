# ⚡ Day 016 — Audio, Video and iFrames Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 🔹 Audio

    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>

Used to embed audio.

---

## 🔹 Video

    <video controls width="640">
        <source src="video.mp4" type="video/mp4">
    </video>

Used to embed video.

---

## 🔹 Common Media Attributes

| Attribute | Purpose |
|---|---|
| `controls` | Shows playback controls |
| `autoplay` | Requests automatic playback |
| `muted` | Starts media without sound |
| `loop` | Repeats media |
| `preload` | Loading hint |
| `poster` | Video preview image |

---

## 🔹 Source

    <source src="audio.mp3" type="audio/mpeg">

Specifies the media file and MIME type.

---

## 🔹 Multiple Sources

    <video controls>

        <source src="video.mp4" type="video/mp4">
        <source src="video.webm" type="video/webm">

    </video>

The browser can select a supported source.

---

## 🔹 Video Captions

    <video controls>

        <source src="lesson.mp4" type="video/mp4">

        <track
            src="captions.vtt"
            kind="captions"
            srclang="en"
            label="English">

    </video>

---

## 🔹 iFrame

    <iframe
        src="https://example.com"
        title="Example Website">
    </iframe>

Used to embed another browsing context.

---

## 🔹 Common iframe Attributes

| Attribute | Purpose |
|---|---|
| `src` | Embedded resource |
| `title` | Accessibility description |
| `width` | Width |
| `height` | Height |
| `loading` | Loading behavior |
| `allow` | Permissions for supported features |
| `sandbox` | Restricts iframe capabilities |
| `referrerpolicy` | Controls referrer information |

---

## 🔹 Lazy Loading

    <iframe
        src="https://example.com"
        title="Example"
        loading="lazy">
    </iframe>

Useful for suitable off-screen embedded content.

---

## 🔹 Audio Formats

Common formats:

- MP3
- Ogg
- WAV

---

## 🔹 Video Formats

Common formats:

- MP4
- WebM
- Ogg

---

## 🔹 Accessibility

For video:

- Use captions when appropriate.
- Provide controls.
- Avoid unexpected sound.

For iframe:

- Always provide a meaningful `title`.

---

## 🔹 Remember

`audio` → Sound

`video` → Video

`source` → Media source

`track` → Captions/timed text

`iframe` → Embedded browsing context

`controls` → Playback controls

`muted` → No sound

`loop` → Repeat

`poster` → Video preview

`sandbox` → Restrict iframe capabilities