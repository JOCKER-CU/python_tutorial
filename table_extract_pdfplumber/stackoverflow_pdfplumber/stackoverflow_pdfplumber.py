import collections
import pdfplumber as pdfplumber


def find_text_parts_on_page(page):
    """
    Idea: separate text by font sizes, rank them by popularity.
    The most popular text size is most likely the main text.
    The second most popular text size is most likely the footnote.
    However, we check which of the two most popular text sizes is larger (by font size).
    We pick the larger one as the main text and the smaller one as the footnote.
    We could also use the vertical position of the bounding box to determine that.
    """

    font_sizes = collections.Counter()
    bounding_boxes = {}

    for char in page.chars:
        size_key = char["size"]
        font_sizes[size_key] += 1
        if size_key not in bounding_boxes:
            bounding_boxes[size_key] = [char["x0"], char["top"], char["x1"], char["bottom"]]
        else:
            if char["x0"] < bounding_boxes[size_key][0]:
                bounding_boxes[size_key][0] = char["x0"]
            if char["top"] < bounding_boxes[size_key][1]:
                bounding_boxes[size_key][1] = char["top"]
            if char["x1"] > bounding_boxes[size_key][2]:
                bounding_boxes[size_key][2] = char["x1"]
            if char["bottom"] > bounding_boxes[size_key][3]:
                bounding_boxes[size_key][3] = char["bottom"]

    most_common_sizes = font_sizes.most_common(2)

    # The main box has larger text size than the footnote box
    first = most_common_sizes[0][0], bounding_boxes[most_common_sizes[0][0]]
    second = most_common_sizes[1][0], bounding_boxes[most_common_sizes[1][0]]

    if first[0] > second[0]:
        return first, second
    else:
        return second, first


with pdfplumber.open(r'C:\Users\hanna\Downloads\DLMM_ACR_FORM-Agent_Confidential_Report_Form-5740f24894744cf9 1.pdf') as pdf:

    first_page = pdf.pages[0]
    [main_size, main_box], [footnote_size, footnote_box] = find_text_parts_on_page(first_page)

    main_part = first_page.within_bbox(main_box)
    footnote_part = first_page.within_bbox(footnote_box)

    print("-----")

    print(main_part.extract_text())

    print("-----")

    print(footnote_part.extract_text())

    print("-----")