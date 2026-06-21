import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "A Moonlight Garden for Samiksha",
  description: "A magical interactive cinematic experience created with love for Samiksha's birthday.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <link
          href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..700&family=Inter:wght@300;400;500;600&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="bg-garden-bg text-garden-text antialiased overflow-hidden select-none">
        {children}
      </body>
    </html>
  );
}