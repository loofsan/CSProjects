const Resource = require("../models/Resource");

/**

 * @param {string} resourceId 
 * @param {number} limit
 * @returns {Array} 
 */
async function findSimilarResources(resourceId, limit = 3) {
  try {
    const resource = await Resource.findById(resourceId);
    if (!resource) {
      throw new Error("Resource not found");
    }

    const query = {
      _id: { $ne: resource._id },
    };

    const typeConditions = [];

    if (resource.type) {
      typeConditions.push({ type: resource.type });
    }

    if (resource.category) {
      typeConditions.push({ category: resource.category });
    }

    if (resource.subcategories && resource.subcategories.length > 0) {
      typeConditions.push({ subcategories: { $in: resource.subcategories } });
    }

    if (resource.services && resource.services.length > 0) {
      typeConditions.push({ services: { $in: resource.services } });
    }

    if (typeConditions.length > 0) {
      query.$or = typeConditions;
    }

    const similarResources = await Resource.find(query).limit(limit).lean();

    if (similarResources.length < limit) {
      return findMoreSimilarResources(resource, similarResources, limit);
    }

    return similarResources;
  } catch (error) {
    console.error("Error finding similar resources:", error);
    return [];
  }
}

/**
 * @param {Object} resource
 * @param {Array} existingResults
 * @param {number} limit
 * @returns {Array}
 */
async function findMoreSimilarResources(resource, existingResults, limit) {
  try {
    const existingIds = existingResults.map((r) => r._id);

    existingIds.push(resource._id);

    const textSearchQuery = {};

    if (resource.description) {
      textSearchQuery.$text = { $search: resource.description };
    }

    textSearchQuery._id = { $nin: existingIds };

    const additionalResources = await Resource.find(textSearchQuery)
      .limit(limit - existingResults.length)
      .lean();

    return [...existingResults, ...additionalResources];
  } catch (error) {
    console.error("Error finding additional similar resources:", error);
    return existingResults;
  }
}

async function updateAllResourceEmbeddings() {
  console.log("Using simplified similarity matching instead of embeddings");
  return;
}

module.exports = {
  findSimilarResources,
  updateAllResourceEmbeddings,
};
