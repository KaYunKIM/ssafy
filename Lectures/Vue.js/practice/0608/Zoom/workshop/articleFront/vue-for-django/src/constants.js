const API_ARTICLE_LIST = API_BASE_URL + '/articles/'
const API_BASE_URL = process.env.NODE_ENV === 'production' ? 'AWS주소' : 'http://localhost:8000'

export {
    API_BASE_URL,
    API_ARTICLE_LIST,
}