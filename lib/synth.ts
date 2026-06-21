"use client";

export class AmbientSynth {
  private ctx: AudioContext | null = null;
  private isPlaying: boolean = false;
  private activeNodes: AudioNode[] = [];
  private sequenceInterval: any = null;

  constructor() {}

  private init() {
    if (this.ctx) return;
    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
    if (AudioContextClass) {
      this.ctx = new AudioContextClass();
    }
  }

  public start() {
    this.init();
    if (!this.ctx || this.isPlaying) return;
    this.isPlaying = true;

    const masterGain = this.ctx.createGain();
    masterGain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    masterGain.connect(this.ctx.destination);
    this.activeNodes.push(masterGain);

    const chords = [
      [174.61, 220.00, 261.63, 329.63], 
      [261.63, 329.63, 392.00, 493.88], 
      [220.00, 261.63, 329.63, 440.00], 
      [196.00, 246.94, 293.66, 392.00], 
    ];

    let step = 0;
    const playNote = (freq: number, startTime: number, duration: number) => {
      if (!this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, startTime);

      gain.gain.setValueAtTime(0, startTime);
      gain.gain.linearRampToValueAtTime(0.12, startTime + 0.5);
      gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

      osc.connect(gain);
      gain.connect(masterGain);

      osc.start(startTime);
      osc.stop(startTime + duration);
    };

    const playStep = () => {
      if (!this.ctx || !this.isPlaying) return;
      const now = this.ctx.currentTime;
      const chord = chords[step % chords.length];

      chord.forEach((freq, idx) => {
        playNote(freq, now + idx * 0.7, 5);
      });

      if (Math.random() > 0.4) {
        const highNote = chord[Math.floor(Math.random() * chord.length)] * 2;
        playNote(highNote, now + 3.0, 3);
      }

      step++;
    };

    playStep();
    this.sequenceInterval = setInterval(playStep, 6000);
  }

  public stop() {
    this.isPlaying = false;
    if (this.sequenceInterval) {
      clearInterval(this.sequenceInterval);
      this.sequenceInterval = null;
    }
    this.activeNodes.forEach((node) => {
      try {
        (node as any).disconnect();
      } catch (e) {}
    });
    this.activeNodes = [];
    if (this.ctx && this.ctx.state !== "closed") {
      this.ctx.close();
      this.ctx = null;
    }
  }
}