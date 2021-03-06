 SELECT news.id,
    news."sophoraId",
    news."externalId",
    news.title,
    news."teaserImageTitle",
    news."teaserImageCopyright",
    news."teaserImageAlttext",
    news."teaserImageType",
    news.date,
    news."updateCheckUrl",
    news."regionId",
    news.details,
    news.detailsweb,
    news.topline,
    news."firstSentence",
    news.ressort,
    news.type,
    news."breakingNews",
    news.index,
    news."insertTime",
    news."crawlTime",
    news."crawlType",
    EXTRACT(hour FROM news.date) + 2::numeric AS hour
   FROM news
  ORDER BY (EXTRACT(hour FROM news.date));