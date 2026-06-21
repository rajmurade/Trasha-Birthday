"use client";
import dynamic from "next/dynamic";

const StarField = dynamic(
  () => import("./StarField").then((m) => m.StarField),
  { ssr: false }
);

const ParticleLayer = dynamic(
  () => import("./ParticleLayer").then((m) => m.ParticleLayer),
  { ssr: false }
);
export function BackgroundScene() {
  return (
    <div className="absolute inset-0 w-full h-full bg-[#05050a] overflow-hidden -z-10 select-none">
      <div 
        className="absolute w-[60vw] h-[60vw] rounded-full blur-[140px] opacity-25 pointer-events-none"
        style={{
          top: "15%",
          left: "20%",
          background: "radial-gradient(circle, #ffb3d1 0%, rgba(255,179,209,0) 70%)"
        }}
      />
      
      <div 
        className="absolute w-[70vw] h-[70vw] rounded-full blur-[160px] opacity-20 pointer-events-none"
        style={{
          bottom: "10%",
          right: "15%",
          background: "radial-gradient(circle, #ffd6e7 0%, rgba(255,214,231,0) 75%)"
        }}
      />

      <div 
        className="absolute w-[50vw] h-[50vw] rounded-full blur-[130px] opacity-[0.12] pointer-events-none"
        style={{
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          background: "radial-gradient(circle, #f7c8da 0%, rgba(247,200,218,0) 70%)"
        }}
      />

      <StarField />
      <ParticleLayer />

      <div className="absolute inset-0 bg-vignette-radial pointer-events-none" />
    </div>
  );
}