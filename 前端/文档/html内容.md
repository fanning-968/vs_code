好的，我将前端开发中最常用的 HTML 标签及其核心属性整理如下，分为结构标签、内容标签、表单标签和媒体标签四类：

---

### **一、结构布局标签（骨架）**

| 标签          | 说明                 | 常用属性                                 |
| ------------- | -------------------- | ---------------------------------------- |
| `<div>`     | 通用容器             | `class`, `id`, `style`, `data-*` |
| `<span>`    | 行内容器             | `class`, `id`, `style`             |
| `<header>`  | 页面/区域头部        | `class`, `id`                        |
| `<footer>`  | 页面/区域底部        | `class`, `id`                        |
| `<main>`    | 页面主要内容         | `class`, `id`                        |
| `<section>` | 文档独立区块         | `class`, `id`                        |
| `<article>` | 独立内容块（如文章） | `class`, `id`                        |
| `<nav>`     | 导航区域             | `class`, `id`                        |
| `<aside>`   | 侧边栏/附属内容      | `class`, `id`                        |
| `<ul>`      | 无序列表             | `class`, `id`                        |
| `<ol>`      | 有序列表             | `class`, `id`, `start`             |
| `<li>`      | 列表项               | `class`, `id`                        |

---

### **二、内容标签（信息展示）**

| 标签              | 说明             | 常用属性                                                              |
| ----------------- | ---------------- | --------------------------------------------------------------------- |
| `<h1>`-`<h6>` | 标题             | `class`, `id`                                                     |
| `<p>`           | 段落             | `class`, `id`                                                     |
| `<a>`           | 超链接           | `href`, `target`（如 `_blank`）, `rel`（SEO）                 |
| `<img>`         | 图片             | `src`, `alt`（必填！）, `width`, `height`, `loading="lazy"` |
| `<strong>`      | 强调内容（粗体） | `class`, `id`                                                     |
| `<em>`          | 强调内容（斜体） | `class`, `id`                                                     |
| `<br>`          | 换行             | -                                                                     |
| `<hr>`          | 水平分割线       | `class`, `id`                                                     |
| `<table>`       | 表格             | `class`, `id`                                                     |
| `<tr>`          | 表格行           | -                                                                     |
| `<td>`          | 表格单元格       | `colspan`, `rowspan`（跨列/行）                                   |
| `<th>`          | 表头单元格       | `scope`（辅助阅读器）                                               |

---

### **三、表单标签（用户交互）**

| 标签           | 说明         | 核心属性                                                                                                                                    |
| -------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `<form>`     | 表单容器     | `action`, `method`（GET/POST）, `autocomplete`                                                                                        |
| `<input>`    | 输入控件     | `type`（text/password/email/number/checkbox/radio/file/date/submit...）, `name`, `value`, `placeholder`, `required`, `disabled` |
| `<textarea>` | 多行文本输入 | `name`, `rows`, `cols`, `placeholder`, `required`                                                                                 |
| `<select>`   | 下拉选择框   | `name`, `multiple`, `required`                                                                                                        |
| `<option>`   | 下拉选项     | `value`, `selected`                                                                                                                     |
| `<button>`   | 按钮         | `type`（submit/reset/button）, `disabled`                                                                                               |
| `<label>`    | 表单标签     | `for`（绑定输入框id）                                                                                                                     |
| `<fieldset>` | 表单分组     | `disabled`                                                                                                                                |
| `<legend>`   | 分组标题     | -                                                                                                                                           |

---

### **四、媒体标签**

| 标签         | 说明       | 核心属性                                                 |
| ------------ | ---------- | -------------------------------------------------------- |
| `<video>`  | 视频播放器 | `src`, `controls`, `autoplay`, `loop`, `muted` |
| `<audio>`  | 音频播放器 | `src`, `controls`, `autoplay`, `loop`            |
| `<iframe>` | 内嵌网页   | `src`, `width`, `height`, `title`（必填！）      |

---

### **五、全局通用属性（所有标签都支持）**

| 属性                | 说明                                            |
| ------------------- | ----------------------------------------------- |
| `class`           | CSS 类名（多个用空格分隔）                      |
| `id`              | 唯一标识符（页面内唯一）                        |
| `style`           | 内联 CSS 样式                                   |
| `data-*`          | 自定义数据属性（如 `data-user-id="123"`）     |
| `title`           | 提示文本（鼠标悬停时显示）                      |
| `hidden`          | 隐藏元素（布尔属性）                            |
| `tabindex`        | Tab 键导航顺序（`0`=可聚焦，`-1`=不可聚焦） |
| `lang`            | 内容语言（如 `en`/`zh-CN`）                 |
| `contenteditable` | 使元素内容可编辑（布尔属性）                    |

---

### **关键使用原则**

1. **语义化优先**用 `<nav>` 代替 `<div class="nav">`，用 `<button>` 代替 `<div class="btn">`
2. **可访问性**

   - 图片必须加 `alt` 描述
   - 表单必须关联 `<label for="id">`
   - 使用 `aria-*` 属性增强屏幕阅读器支持
3. **响应式设计**

   - 图片：`srcset` + `sizes` 属性
   - 视频：`<source>` 子标签适配不同格式
4. **性能优化**

   - 图片：`loading="lazy"`
   - 脚本：`<script defer>` 或 `<script async>`

> 完整标签参考：[MDN HTML 元素参考](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element)
> 现代 HTML 开发应结合 CSS 和 JavaScript 使用，避免使用废弃属性（如 `<table border="1">` 改用 CSS 实现）。
>
