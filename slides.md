---
marp: true
theme: default
paginate: true
---


<!-- Custom theme definition -->
<style>
section {
  font-family: "Helvetica", sans-serif;
}
h1 {
  color: #1e88e5;
}
footer {
  font-size: 12px;
  color: #666;
}
</style>

<!-- Custom Theme -->
<style>
:root {
  --background: #ffffff;
  --foreground: #222222;
  --accent: #1e88e5;
}
</style>

<!-- Footer with page numbers -->
<footer>Page ${page} / ${total}</footer>

# Product Documentation Presentation  
### Using **Marp** for Technical Writing  
**By:** Aditya Jha  
📧 **24f2005506@ds.study.iitm.ac.in**

---

# Why Marp?

- Markdown-based → easy version control  
- Export to PDF, PPTX, HTML  
- Custom themes using CSS  
- Supports diagrams, math, and backgrounds  

---

<!-- Slide with background image -->
<!-- Replace the image URL with your own -->
![bg](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200)

# Background Image Slide  
Marp allows easy slide-level background customization using directives.

---

# Custom Styling Example

This text is *italic*  
This text is **bold**  
This text is <span style="color:#e53935; font-weight:bold;">custom styled using inline CSS</span>  

---

# Math Support (Algorithmic Complexity)

Marp supports LaTeX-style math using KaTeX:

$$
T(n) = O(n \log n)
$$

Another example:

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

---

# Custom Theme Definition

You can also create a separate theme file (e.g., `theme.css`) and use it:

```css
@charset "UTF-8";
:root {
  --color-primary: #1e88e5;
}
section {
  padding: 60px;
}
h1 {
  color: var(--color-primary);
}
