from types.bundle import BundleQuery
from graphene import String, Schema


class Query(BundleQuery):
    """
    Query fields (i.e. methods on this class) are top-level fields in the GraphQL schema
    which are designed to return data.  Queries do not alter state.

    If you want to save, delete, update, or otherwise trigger actions that alter state, use the Mutation class.
    """
    bundle = String(name=String(default_value="Temporary Bundle"))

    def resolve_bundle(root) -> String:
        """
        The Bundle resolver.  This is a temporary method which is to be removed.

        What will replace this will be standard interfaces for each type.
        This will include:

        * get_bundle(id)
        * get_bundles(search_options)
            * Note that for search_options, what you can search will vary by type
            * In this case, for example, you can search by bundle name or type
            * You can also search by products
        * get_product(id)
        * get_products(search_options)
            * You can use this to search for all products that are ebooks
            * You can combine multiple search terms to find all ebooks that are .epub and have the word "python" in their title
        :return: The temporary bundle
        :rtype: String
        """
        return f'This is a temporary bundle placeholder'

    def resolve_get_bundles(root):
        return list(cache.get("orders").keys())

schema = Schema(query=Query)