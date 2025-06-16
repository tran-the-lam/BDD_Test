# Hướng dẫn kiểm thử E-commerce Application

## Cách sử dụng file USER_STORIES.md

File `USER_STORIES.md` chứa tất cả các user stories được tổ chức theo module. Mỗi user story có:
- **ID**: US-XXX để dễ theo dõi
- **Mô tả**: Vai trò và mục đích của user story
- **Acceptance Criteria**: Các điều kiện cần thỏa mãn để pass test

## Test Cases theo Priority

### 🔥 HIGH PRIORITY - Core Functions

#### 1. Authentication Flow
```
✅ US-001: Đăng nhập thành công
- Email: john@example.com
- Password: password123
- Expected: Hiển thị "John Doe" trên header

✅ US-002: Đăng nhập thất bại
- Email: wrong@email.com
- Password: wrongpass
- Expected: "Invalid email or password"

✅ US-004: Đăng ký thành công
- Tạo tài khoản mới với email chưa tồn tại
- Expected: Tự động đăng nhập sau khi đăng ký
```

#### 2. Shopping Cart Flow
```
✅ US-020: Thêm sản phẩm vào giỏ
- Click "Add to Cart" trên bất kỳ sản phẩm nào
- Expected: Cart icon hiển thị số lượng

✅ US-023: Xem giỏ hàng
- Click cart icon
- Expected: Sidebar hiển thị danh sách sản phẩm

✅ US-024: Cập nhật số lượng
- Click +/- trong cart
- Expected: Total cập nhật real-time
```

#### 3. Product Management
```
✅ US-011: Hiển thị danh sách sản phẩm
- Load trang chủ
- Expected: Grid hiển thị 8 sản phẩm

✅ US-012: Xem chi tiết sản phẩm
- Click vào sản phẩm hoặc icon mắt
- Expected: Modal hiển thị thông tin chi tiết
```

### 🟡 MEDIUM PRIORITY - Enhanced Features

#### 4. Search & Filter
```
✅ US-017: Tìm kiếm sản phẩm
- Nhập "headphones" vào search box
- Expected: Hiển thị sản phẩm liên quan

✅ US-014: Lọc theo danh mục
- Chọn "Electronics" trong filters
- Expected: Chỉ hiển thị sản phẩm Electronics

✅ US-015: Lọc theo giá
- Set price range 200-500
- Expected: Chỉ hiển thị sản phẩm trong khoảng giá
```

#### 5. Profile Management
```
✅ US-007: Xem profile
- Click tên user → "Profile & Orders"
- Expected: Modal hiển thị thông tin cá nhân

✅ US-008: Chỉnh sửa profile
- Click "Edit" → Sửa thông tin → "Save"
- Expected: Thông tin được cập nhật
```

### 🟢 LOW PRIORITY - Edge Cases

#### 6. Error Handling
```
✅ US-018: Tìm kiếm không có kết quả
- Search "xyz123"
- Expected: "No products found"

✅ US-022: Sản phẩm hết hàng
- Thử add "Wireless Gaming Mouse"
- Expected: Button disabled, không thể add

✅ US-027: Giỏ hàng trống
- Clear cart hoặc chưa add gì
- Expected: Empty state với icon và message
```

## Quick Test Scenarios

### Scenario 1: Happy Path (5 phút)
1. Đăng nhập với john@example.com / password123
2. Search "headphones"
3. Add sản phẩm vào cart
4. Xem cart và update quantity
5. Proceed to checkout
6. Hoàn tất đặt hàng

### Scenario 2: Error Handling (3 phút)
1. Thử đăng nhập sai thông tin
2. Thử add sản phẩm hết hàng
3. Search từ khóa không tồn tại
4. Thử checkout khi chưa đăng nhập

### Scenario 3: Mobile Testing (3 phút)
1. Resize browser xuống mobile size
2. Test hamburger menu
3. Test filters toggle
4. Test cart sidebar

## Automated Testing Checklist

Để kiểm tra nhanh tất cả functions:

```bash
# 1. Load trang chủ
- ✅ Hiển thị 8 sản phẩm
- ✅ Header có search box và cart icon
- ✅ Filters sidebar hiển thị categories

# 2. Test Authentication
- ✅ Click "Sign In" → Modal mở
- ✅ Login với demo account
- ✅ Header hiển thị user name

# 3. Test Shopping
- ✅ Add 2-3 sản phẩm vào cart
- ✅ Cart icon hiển thị số lượng
- ✅ Open cart → Xem danh sách

# 4. Test Search/Filter
- ✅ Search "camera" → Có kết quả
- ✅ Filter "Electronics" → Lọc đúng
- ✅ Clear filters → Reset về All

# 5. Test Responsive
- ✅ Mobile: Menu collapse
- ✅ Tablet: Layout responsive
- ✅ Desktop: Full features
```

## Bug Report Template

Khi tìm thấy bug, report theo format:

```
**User Story**: US-XXX
**Steps to Reproduce**:
1. Step 1
2. Step 2
3. Step 3

**Expected Result**: 
**Actual Result**: 
**Browser**: Chrome/Firefox/Safari
**Screen Size**: Desktop/Tablet/Mobile
```

## Performance Checklist

- ✅ Trang load < 3 giây
- ✅ Search results hiển thị real-time
- ✅ Cart updates không lag
- ✅ Modal animations smooth
- ✅ Images load properly
- ✅ No console errors

Sử dụng file này để kiểm thử có hệ thống và đảm bảo tất cả user stories được cover!