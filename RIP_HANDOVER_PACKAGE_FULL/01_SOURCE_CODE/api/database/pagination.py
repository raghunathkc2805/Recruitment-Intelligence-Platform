from math import ceil


class Pagination:

    @staticmethod
    def paginate(query, page=1, page_size=50):

        total = query.count()

        records = query.offset(
            (page-1)*page_size
        ).limit(
            page_size
        ).all()

        return {

            "page": page,

            "page_size": page_size,

            "total_records": total,

            "total_pages": ceil(total/page_size) if total else 0,

            "items": records,

        }
