📋 Day 008 — HTML Forms Cheat Sheet
📝 Basic Form
<form>
    <!-- form elements -->
</form>
🏷️ Label
<label for="name">Name:</label>
<input type="text" id="name">

for → जिस input से label जुड़ा है उसकी id बताता है।

⌨️ Input Types
<input type="text">
<input type="email">
<input type="password">
<input type="number">
<input type="date">
<input type="tel">
<input type="url">
<input type="file">
Radio Button
<input type="radio" name="gender" value="male"> Male
<input type="radio" name="gender" value="female"> Female

👉 Same name होने पर एक option select होगा।

Checkbox
<input type="checkbox" name="skill" value="html"> HTML
<input type="checkbox" name="skill" value="css"> CSS

👉 Multiple options select कर सकते हैं।

📋 Select / Dropdown
<select name="course">
    <option value="html">HTML</option>
    <option value="css">CSS</option>
    <option value="javascript">JavaScript</option>
</select>
📝 Textarea
<textarea name="message" rows="5" cols="30"></textarea>

👉 लंबे text/message के लिए।

🔘 Button
<button type="submit">Submit</button>
<button type="reset">Reset</button>
<button type="button">Click Me</button>
Common Button Types
Type	काम
submit	Form submit
reset	Form reset
button	Normal button
⭐ Important Attributes
<input
    type="text"
    id="name"
    name="username"
    placeholder="Enter your name"
    required
>
याद रखें:
id → Element की पहचान
name → Form data का नाम
value → Element की value
placeholder → Hint text
required → Field भरना जरूरी
disabled → Input को disable करता है
readonly → Value बदल नहीं सकते
📤 Complete Form Structure
<form action="/submit" method="post">

    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <br><br>

    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>

    <br><br>

    <button type="submit">Submit</button>

</form>
🚀 Quick Revision

Form → Label → Input → Select → Textarea → Button

सबसे important:

<form>
<label>
<input>
<select>
<option>
<textarea>
<button>
🔥 Exam/Project में सबसे ज्यादा याद रखने वाले
<form action="" method="post">

<input type="text">
<input type="email">
<input type="password">

<input type="radio">
<input type="checkbox">

<select>
<option>

<textarea></textarea>

<button type="submit">Submit</button>

</form>