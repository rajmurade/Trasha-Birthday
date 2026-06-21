import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        garden: {
          bg: "#05050a",
          glowPrimary: "#ffd6e7",
          glowSecondary: "#ffb3d1",
          text: "#fff8fb",
          accent: "#f7c8da",
          darkMuted: "#1a1525",
        },
      },
      fontFamily: {
        serif: ["var(--font-serif)", "Georgia", "serif"],
        sans: ["var(--font-sans)", "Inter", "sans-serif"],
      },
      backgroundImage: {
        "vignette-radial": "radial-gradient(circle, transparent 40%, rgba(5,5,10,0.95) 100%)",
        "glow-radial": "radial-gradient(circle, var(--tw-gradient-stops))",
      },
    },
  },
  plugins: [],
};
export default config;