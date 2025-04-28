const mongoose = require("mongoose");

const hourSchema = new mongoose.Schema({
  day: { type: Number, required: true },
  open: { type: String, default: "" },
  close: { type: String, default: "" },
});

const resourceSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      index: true,
    },
    type: {
      type: String,
      index: true,
    },
    category: {
      type: String,
      index: true,
    },
    subcategories: [
      {
        type: String,
        index: true,
      },
    ],
    description: {
      type: String,
    },

    location: {
      type: {
        type: String,
        enum: ["Point"],
        required: true,
      },
      coordinates: {
        type: [Number],
        required: true,
      },
    },

    address: {
      type: String,
    },
    contact: {
      phone: { type: String },
      email: { type: String },
      website: { type: String },
    },

    contactPhone: { type: String },

    hours: [hourSchema],

    requirements: [{ type: String }],
    eligibility: { type: String },
    documentation_required: [{ type: String }],
    languages: [{ type: String }],
    accessibility: [{ type: String }],
    services: [{ type: String }],
    restrictions: [{ type: String }],
    currentCapacity: { type: Number },
    totalCapacity: { type: Number },
    capacity: { type: String },
    lastUpdated: { type: Date, default: Date.now },
    website: { type: String },

    verificationStatus: {
      type: String,
      enum: ["pending", "verified", "rejected"],
      default: "pending",
    },
    submittedAt: { type: Date },
    submittedBy: { type: String },
  },
  {
    timestamps: true,

    strict: false,
  }
);

resourceSchema.index({
  name: "text",
  description: "text",
  address: "text",
  eligibility: "text",
  services: "text",
});

resourceSchema.index({ location: "2dsphere" });

resourceSchema.virtual("categoryFromType").get(function () {
  const typeToCategory = {
    shelter: "housing",
    "food bank": "food",
    "medical clinic": "healthcare",
    "employment center": "employment",
  };

  return this.category || typeToCategory[this.type] || "other";
});

resourceSchema.add({
  embedding: {
    type: [Number],
    index: false,
    default: null,
  },
});

resourceSchema.index(
  { embedding: "vectorSearch" },
  {
    vectorSearchOptions: {
      dimension: 768,
      similarity: "cosine",
    },
  }
);

const Resource = mongoose.model("Resource", resourceSchema);

module.exports = Resource;
