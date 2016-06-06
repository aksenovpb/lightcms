from lightcms.applications_pool import applications_pool


class ArticleApp():
    app = 'articles'

applications_pool.register(ArticleApp)
