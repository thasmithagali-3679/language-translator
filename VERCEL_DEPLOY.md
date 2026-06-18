# Vercel Deployment Guide

## 🚀 Deploy to Vercel

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy from your project folder
```bash
vercel
```

### Step 4: For production deployment
```bash
vercel --prod
```

## 📱 Usage

### GET Request:
```
https://your-app.vercel.app/api/translate?text=Hello&source=en&target=es
```

### POST Request:
```json
{
  "text": "Hello",
  "source": "en",
  "target": "es"
}
```

## 🌐 Test on Android
Open this in your phone browser:
```
https://your-app.vercel.app/api/translate?text=Hello&target=fr
```

## ✅ Notes
- This version runs as a Vercel serverless API
- It is great for mobile/browser use
- If you want a full web UI on Vercel, I can also convert your Streamlit app into plain HTML/CSS/JavaScript next
