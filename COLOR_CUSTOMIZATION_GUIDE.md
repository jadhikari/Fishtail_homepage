# Fishtail Brand Color Customization Guide

## How to Customize Colors to Match Your Logo

The header and footer now use custom CSS variables that you can easily adjust to match your logo colors.

### Current Color Scheme
- **Primary**: Deep blue (#1e3a8a)
- **Secondary**: Lighter blue (#3b82f6) 
- **Accent**: Orange (#f59e0b)

### To Change Colors:

1. **Open the CSS file**: `/static/css/fishtail-brand.css`

2. **Find the CSS variables section** (lines 2-8):
```css
:root {
    --fishtail-primary: #1e3a8a; /* Deep blue - adjust to match your logo */
    --fishtail-secondary: #3b82f6; /* Lighter blue - adjust to match your logo */
    --fishtail-accent: #f59e0b; /* Orange accent - adjust to match your logo */
    --fishtail-text-light: #ffffff;
    --fishtail-text-dark: #1f2937;
}
```

3. **Replace the hex color codes** with your logo colors:
   - `--fishtail-primary`: Main color from your logo
   - `--fishtail-secondary`: Secondary color from your logo  
   - `--fishtail-accent`: Accent/highlight color from your logo

### Example:
If your logo uses:
- Main color: #2c5530 (dark green)
- Secondary color: #4ade80 (light green)
- Accent color: #fbbf24 (yellow)

Change the CSS to:
```css
:root {
    --fishtail-primary: #2c5530; /* Dark green */
    --fishtail-secondary: #4ade80; /* Light green */
    --fishtail-accent: #fbbf24; /* Yellow accent */
    --fishtail-text-light: #ffffff;
    --fishtail-text-dark: #1f2937;
}
```

### Features Included:
- ✅ Gradient backgrounds using your logo colors
- ✅ Smooth hover animations
- ✅ Professional shadows and borders
- ✅ Responsive design for mobile devices
- ✅ Consistent branding across header and footer
- ✅ Easy color customization via CSS variables

### After Making Changes:
1. Save the CSS file
2. Refresh your browser to see the changes
3. The colors will automatically apply to both header and footer

### Need Help Finding Logo Colors?
You can use online color picker tools or browser developer tools to identify the exact hex codes from your logo image.
