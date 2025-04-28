const express = require("express");
const router = express.Router();
const Resource = require("../models/Resource");
const { findSimilarResources } = require("../services/embeddingService");

router.get("/", async (req, res) => {
  try {
    const resources = await Resource.find();
    res.json(resources);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get("/:id", async (req, res) => {
  try {
    const resource = await Resource.findById(req.params.id);
    if (!resource) {
      return res.status(404).json({ message: "Resource not found" });
    }
    res.json(resource);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get("/category/:category", async (req, res) => {
  try {
    const resources = await Resource.find({ category: req.params.category });
    res.json(resources);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get("/subcategory/:subcategory", async (req, res) => {
  try {
    const resources = await Resource.find({
      subcategories: req.params.subcategory,
    });
    res.json(resources);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get("/nearby/:longitude/:latitude/:maxDistance?", async (req, res) => {
  try {
    const longitude = parseFloat(req.params.longitude);
    const latitude = parseFloat(req.params.latitude);
    const maxDistance = req.params.maxDistance
      ? parseInt(req.params.maxDistance)
      : 5000;

    if (isNaN(longitude) || isNaN(latitude)) {
      return res.status(400).json({ message: "Invalid coordinates" });
    }

    const resources = await Resource.find({
      "location.coordinates": {
        $near: {
          $geometry: {
            type: "Point",
            coordinates: [longitude, latitude],
          },
          $maxDistance: maxDistance,
        },
      },
    });

    res.json(resources);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.get("/:id/similar", async (req, res) => {
  try {
    const resourceId = req.params.id;
    const limit = parseInt(req.query.limit) || 3;

    const similarResources = await findSimilarResources(resourceId, limit);

    res.json(similarResources);
  } catch (error) {
    console.error("Error getting similar resources:", error);
    res.status(500).json({ message: error.message });
  }
});

router.post("/", async (req, res) => {
  try {
    if (!req.body.name || !req.body.address) {
      return res.status(400).json({ message: "Name and address are required" });
    }

    const resourceData = {
      ...req.body,
      location: req.body.location || {
        type: "Point",
        coordinates: [0, 0],
      },
      verificationStatus: "pending",
      submittedAt: new Date(),
    };

    const resource = new Resource(resourceData);
    const newResource = await resource.save();

    console.log(
      `New resource submitted: ${newResource.name} (ID: ${newResource._id})`
    );

    res.status(201).json({
      success: true,
      message: "Resource submitted successfully and pending review",
      resource: {
        id: newResource._id,
        name: newResource.name,
      },
    });
  } catch (err) {
    console.error("Error creating resource:", err);
    res.status(400).json({
      success: false,
      message: err.message,
    });
  }
});
router.patch("/:id", async (req, res) => {
  try {
    const updatedResource = await Resource.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    res.json(updatedResource);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

router.delete("/:id", async (req, res) => {
  try {
    await Resource.findByIdAndDelete(req.params.id);
    res.json({ message: "Resource deleted" });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
