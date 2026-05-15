import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

frontend_dir = r"c:\Users\suyas\IPL\frontend\src"

# Update layout.tsx
layout_content = """import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "IPL Auction Pro",
  description: "Advanced IPL Auction Simulator",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-[#0A0F1E] text-[#F9FAFB] min-h-screen`}>{children}</body>
    </html>
  );
}
"""
create_file(os.path.join(frontend_dir, "app", "layout.tsx"), layout_content)

# Update page.tsx
page_content = """import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 text-center">
      <h1 className="text-6xl font-bold text-[#F59E0B] mb-8 uppercase tracking-widest font-clash">
        IPL Auction Pro
      </h1>
      <p className="text-xl text-[#9CA3AF] mb-12 max-w-2xl font-satoshi">
        The ultimate real-time IPL Cricket Auction Simulator. Create a room, assemble your dream squad, and get AI-powered post-auction analysis.
      </p>
      
      <div className="flex gap-6">
        <Link 
          href="/create"
          className="px-8 py-4 bg-gradient-to-r from-[#F59E0B] to-yellow-600 rounded-xl text-black font-bold text-lg hover:scale-105 transition-transform shadow-lg shadow-yellow-500/20"
        >
          Create Room
        </Link>
        <Link 
          href="/join"
          className="px-8 py-4 bg-[#111827] border border-[#1F2937] rounded-xl text-white font-bold text-lg hover:bg-gray-800 transition-colors"
        >
          Join Room
        </Link>
      </div>
    </main>
  );
}
"""
create_file(os.path.join(frontend_dir, "app", "page.tsx"), page_content)

# Create global css
css_content = """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #0A0F1E;
  --foreground: #F9FAFB;
}

body {
  color: var(--foreground);
  background: var(--background);
}
"""
create_file(os.path.join(frontend_dir, "app", "globals.css"), css_content)

print("Frontend scaffold scripts generated.")
