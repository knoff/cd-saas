import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// билд сразу в backend/app/static/web
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../backend/app/static/web',
    emptyOutDir: true,
  },
});
