#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> card, vector<string> word) {
	vector<string> answer = {};

	string::iterator it;
	vector<int>::iterator vit;
	int i, j, k;
	bool bFind;

	// 1. 총 단어 수
	for (i = 0, bFind = true; i < word.size(); i++, bFind = true)
	{
		// 2. 단어별 검색
		vector<string> cpCard(card);
		vector<int> isVisit = { 0, 1, 2 }; // 1~3세트 방문 체크

		for (j = 0; j < word[i].size(); j++)
		{
			// 단어마다 카드를 새로 생성
			// 3. 카드별 탐색
			for (k = 0; k < 3; k++)
			{
				it = find(cpCard[k].begin(), cpCard[k].end(), word[i].at(j));
				if (it != cpCard[k].end())
				{
					// 사용한 카드 삭제
					cpCard[k].erase(it);

					// 방문한 세트 번호는 삭제
					vit = find(isVisit.begin(), isVisit.end(), k);

					if (vit != isVisit.end()) isVisit.erase(vit);
					break;
				}
			}

			// 알파벳이 없을 때
			if (k == 3)
			{
				bFind = false;
				break;
			}
		}

		// 1~3세트 카드 모두 방문하였는지 체크
		if (isVisit.size() != 0)
			bFind = false;

		if (bFind)
			answer.push_back(word[i]);
	}

	if (answer.size() == 0)
		answer.push_back("-1");

	return answer;
}

int main()
{
	vector<string> cards = {
	"ABACDEFG",
	"NOPQRSTU",
	"HIJKLKMM"
	};
	// vector<string> words = { "GPQM", "GPMZ", "EFU", "MMNA" };
	vector<string> words = { "AACDPQRJMM", "ANOEFTMHILMZ" };

	vector<string> answer = solution(cards, words);
	for (int i = 0; i < answer.size(); i++)
	{
		cout << answer[i] << " ";
	}
	cout << endl;
}