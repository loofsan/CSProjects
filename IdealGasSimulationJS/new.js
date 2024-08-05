function randomNumBetween(min, max) {
  return min + Math.random() * (max - min);
}

function sampleMaxwellBoltzmann(speedMean) {
  const rand1 = Math.random();
  const rand2 = Math.random();
  const rand3 = Math.random();
  const speed =
    speedMean * Math.sqrt(-2 * Math.log(rand1)) * Math.cos(2 * Math.PI * rand2);
  const angle = 2 * Math.PI * rand3;
  return { speed, angle };
}

class Vector {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  static add(vector1, vector2) {
    return new Vector(vector1.x + vector2.x, vector1.y + vector2.y);
  }
  static mult(vector, scalar) {
    return new Vector(vector.x * scalar, vector.y * scalar);
  }
  static div(vector, scalar) {
    return new Vector(vector.x / scalar, vector.y / scalar);
  }
  static sub(vector1, vector2) {
    return new Vector(vector1.x - vector2.x, vector1.y - vector2.y);
  }
  dot(vector) {
    return this.x * vector.x + this.y * vector.y;
  }
  getTangent() {
    return new Vector(-this.y, this.x);
  }
  mag() {
    return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
  }
  copy() {
    return new Vector(this.x, this.y);
  }
  static random(minX, maxX, minY, maxY) {
    return new Vector(
      randomNumBetween(minX, maxX),
      randomNumBetween(minY, maxY)
    );
  }
}

class Particle {
  constructor(x, y) {
    this.pos = new Vector(x, y);
    this.vel = Vector.random(-1, 1, -1, 1);
    this.acc = new Vector(0, 0);
    this.radius = 5;
    this.setInitialVelocity();
  }
  setInitialVelocity() {
    const { speed, angle } = sampleMaxwellBoltzmann(2); // Adjust mean speed as needed
    this.vel = new Vector(speed * Math.cos(angle), speed * Math.sin(angle));
  }
  update() {
    this.pos = Vector.add(this.pos, this.vel);
    this.vel = Vector.add(this.vel, this.acc);
    this.acc = Vector.mult(this.acc, 0);
  }
  checkCollision(particle) {
    const v = Vector.sub(this.pos, particle.pos);
    const dist = v.mag();
    if (dist <= this.radius + particle.radius) {
      const unitNormal = Vector.div(v, v.mag());
      const unitTangent = unitNormal.getTangent();

      const correction = Vector.mult(unitNormal, this.radius + particle.radius);
      const newV = Vector.add(particle.pos, correction);
      this.pos = newV;

      const a = this.vel;
      const b = particle.vel;

      const a_n = a.dot(unitNormal);
      const b_n = b.dot(unitNormal);
      const a_t = a.dot(unitTangent);
      const b_t = b.dot(unitTangent);

      const a_n_final =
        (a_n * (this.radius - particle.radius) + 2 * particle.radius * b_n) /
        (this.radius + particle.radius);
      const b_n_final =
        (b_n * (particle.radius - this.radius) + 2 * this.radius * a_n) /
        (this.radius + particle.radius);

      const a_n_after = Vector.mult(unitNormal, a_n_final);
      const b_n_after = Vector.mult(unitNormal, b_n_final);
      const a_t_after = Vector.mult(unitTangent, a_t);
      const b_t_after = Vector.mult(unitTangent, b_t);

      const a_after = Vector.add(a_n_after, a_t_after);
      const b_after = Vector.add(b_n_after, b_t_after);

      this.vel = a_after;
      particle.vel = b_after;
    }
  }
  handleEdges(width, height) {
    if (this.pos.x - this.radius <= 0) {
      this.pos.x = this.radius;
      this.vel.x = -this.vel.x;
    } else if (this.pos.x + this.radius >= width) {
      this.pos.x = width - this.radius;
      this.vel.x = -this.vel.x;
    }
    if (this.pos.y - this.radius <= 0) {
      this.pos.y = this.radius;
      this.vel.y = -this.vel.y;
    } else if (this.pos.y + this.radius >= height) {
      this.pos.y = height - this.radius;
      this.vel.y = -this.vel.y;
    }
  }
  speed() {
    return this.vel.mag();
  }
}

class Canvas {
  constructor() {
    this.simCanvas = document.getElementById("simulationCanvas");
    this.simCtx = this.simCanvas.getContext("2d");

    this.simCanvas.width = 800;
    this.simCanvas.height = 800;

    this.histCanvas = document.getElementById("histogramCanvas");
    this.histCtx = this.histCanvas.getContext("2d");

    this.histCanvas.width = 800;
    this.histCanvas.height = 800;

    this.overlayCanvas = document.getElementById("overlayCanvas");
    this.overlayCtx = this.overlayCanvas.getContext("2d");

    this.overlayCanvas.width = 800;
    this.overlayCanvas.height = 800;

    this.temperature = 2; // Initial temperature

    this.setupTemperatureControl();
    this.setup();
    this.setupButtons();
    requestAnimationFrame(() => this.update());
  }
  setup() {
    const NUM_PARTICLES = 100;
    this.particles = [];

    for (let i = 0; i < NUM_PARTICLES; i++) {
      this.particles.push(
        new Particle(
          randomNumBetween(0, this.simCanvas.width),
          randomNumBetween(0, this.simCanvas.height)
        )
      );
    }
  }

  setupTemperatureControl() {
    this.temperatureSlider = document.getElementById("temperatureControl");
    this.temperatureSlider.addEventListener("input", () => {
      this.temperature = parseFloat(this.temperatureSlider.value);
      this.adjustParticleVelocities();
    });
  }

  adjustParticleVelocities() {
    const temperatureRatio = Math.sqrt(this.temperature / 2); // Square root because KE ~ v^2
    for (let particle of this.particles) {
      particle.vel = Vector.mult(particle.vel, temperatureRatio);
    }
  }

  setInitialVelocity(particle) {
    const { speed, angle } = sampleMaxwellBoltzmann(
      Math.sqrt(this.temperature)
    );
    particle.vel = new Vector(speed * Math.cos(angle), speed * Math.sin(angle));
  }

  setupButtons() {
    const addButton = document.getElementById("addParticles");
    addButton.addEventListener("click", () => this.addNewParticles());

    const removeButton = document.getElementById("removeParticles");
    removeButton.addEventListener("click", () => this.removeParticles());

    const resetButton = document.getElementById("resetParticles");
    resetButton.addEventListener("click", () => this.resetSimulation());
  }

  addNewParticles() {
    const newParticles = 10; // Number of particles to add each time
    for (let i = 0; i < newParticles; i++) {
      this.particles.push(
        new Particle(
          randomNumBetween(0, this.simCanvas.width),
          randomNumBetween(0, this.simCanvas.height)
        )
      );
    }
  }
  removeParticles() {
    const particlesToRemove = 10; // Number of particles to remove each time
    if (this.particles.length > particlesToRemove) {
      this.particles.splice(
        this.particles.length - particlesToRemove,
        particlesToRemove
      );
    } else {
      this.particles = []; // Remove all particles if less than particlesToRemove remain
    }
  }

  resetSimulation() {
    this.particles = []; // Clear all particles
    this.updateParticleCountDisplay();
  }

  update() {
    this.simCtx.clearRect(0, 0, this.simCanvas.width, this.simCanvas.height);
    this.histCtx.clearRect(0, 0, this.histCanvas.width, this.histCanvas.height);

    const speeds = [];

    for (let i = 0; i < this.particles.length; i++) {
      const current = this.particles[i];
      const rest = this.particles.slice(i + 1);

      for (let p of rest) {
        p.checkCollision(current);
      }
    }

    for (let particle of this.particles) {
      particle.update();
      particle.handleEdges(this.simCanvas.width, this.simCanvas.height);
      speeds.push(particle.speed());

      this.simCtx.fillStyle = `rgba(255, 255, 255, 1)`;
      this.simCtx.beginPath();
      this.simCtx.arc(
        particle.pos.x,
        particle.pos.y,
        particle.radius,
        0,
        2 * Math.PI
      );
      this.simCtx.fill();
    }

    this.plotHistogram(speeds);
    this.updateParticleCountDisplay();
    this.plotTheoreticalCurve();
    requestAnimationFrame(() => this.update());
  }
  updateParticleCountDisplay() {
    const particleCount = this.particles.length;
    document.getElementById(
      "particleCount"
    ).textContent = `Particles: ${particleCount}`;
  }

  plotHistogram(speeds) {
    const numBins = 20; // Increased number of histogram bars
    const maxSpeed = 10; // Upper limit of velocity for the x-axis
    const minSpeed = 0; // Lower limit of velocity for the x-axis
    const binWidth = (maxSpeed - minSpeed) / numBins;

    const bins = new Array(numBins).fill(0);

    speeds.forEach((speed) => {
      const bin = Math.floor((speed - minSpeed) / binWidth);
      bins[Math.min(bin, bins.length - 1)]++;
    });

    const totalParticles = speeds.length;
    const normalizedBins = bins.map(
      (count) => count / (totalParticles * binWidth)
    );

    const maxBinDensity = Math.max(...normalizedBins);
    const histHeight = this.histCanvas.height;
    const histWidth = this.histCanvas.width;
    const barWidth = histWidth / numBins;

    // Draw axes
    this.histCtx.beginPath();
    this.histCtx.moveTo(50, 10);
    this.histCtx.lineTo(50, histHeight - 50);
    this.histCtx.lineTo(histWidth - 10, histHeight - 50);
    this.histCtx.stroke();

    // Draw x-axis labels
    this.histCtx.fillStyle = "white";
    this.histCtx.textAlign = "center";
    for (let i = 0; i <= numBins; i++) {
      const x = 50 + i * barWidth;
      const speed = minSpeed + i * binWidth;
      this.histCtx.fillText(speed.toFixed(1), x, histHeight - 30);
    }

    // Draw y-axis labels
    this.histCtx.textAlign = "right";
    for (let i = 0; i <= 5; i++) {
      const y = histHeight - 50 - (i / 5) * (histHeight - 60);
      const density = (i / 5) * maxBinDensity;
      this.histCtx.fillText(density.toFixed(2), 40, y);
    }

    // Draw histogram bars
    this.histCtx.fillStyle = "white";
    normalizedBins.forEach((density, index) => {
      const barHeight = (density / maxBinDensity) * (histHeight - 60);
      this.histCtx.fillRect(
        50 + index * barWidth,
        histHeight - 50 - barHeight,
        barWidth,
        barHeight
      );
    });
    this.plotTheoreticalCurve();
  }

  plotTheoreticalCurve() {
    const numPoints = 100;
    const maxSpeed = 10;
    const minSpeed = 0;
    const T = this.temperature;

    const kB = 1; // Boltzmann constant (set to 1 for simplification)
    const m = 1; // Mass of particle (set to 1 for simplification)

    this.overlayCtx.clearRect(
      0,
      0,
      this.overlayCanvas.width,
      this.overlayCanvas.height
    );
    this.overlayCtx.strokeStyle = "yellow";
    this.overlayCtx.lineWidth = 2;
    this.overlayCtx.beginPath();

    let maxF = 0;

    // First pass to find the maximum value of the distribution
    for (let i = 0; i <= numPoints; i++) {
      const v = minSpeed + (i / numPoints) * (maxSpeed - minSpeed);
      const f =
        4 *
        Math.PI *
        Math.pow(v, 2) *
        Math.pow(m / (2 * Math.PI * kB * T), 1.5) *
        Math.exp((-m * v * v) / (2 * kB * T));
      if (f > maxF) maxF = f;
    }

    // Second pass to draw the curve
    for (let i = 0; i <= numPoints; i++) {
      const v = minSpeed + (i / numPoints) * (maxSpeed - minSpeed);
      const f =
        4 *
        Math.PI *
        Math.pow(v, 2) *
        Math.pow(m / (2 * Math.PI * kB * T), 1.5) *
        Math.exp((-m * v * v) / (2 * kB * T));

      const x = 50 + (i / numPoints) * (this.overlayCanvas.width - 60);
      const y =
        this.overlayCanvas.height -
        50 -
        (f / maxF) * (this.overlayCanvas.height - 60);

      if (i === 0) {
        this.overlayCtx.moveTo(x, y);
      } else {
        this.overlayCtx.lineTo(x, y);
      }
    }

    this.overlayCtx.stroke();
  }
}

new Canvas();
