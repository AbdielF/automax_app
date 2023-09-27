def user_listing_path(instance, filename):
    return f'user_{instance.seller.user.id}/listing/{filename}'