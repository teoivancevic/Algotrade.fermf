#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

const int inf=1e9;

map < string, int > ind;
int curr;


vector < pair < int, int > > edge;
vector < __int128 > close, volume;
vector < double > weight;
int n, m;

void bellman_ford(int x){
	double dist[n];
	for(int i=0; i<n; i++){
		dist[i]=inf;
	}
	dist[x]=0;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(dist[edge[j].first]+weight[
		}
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	string s;
	getline(cin, s);
	int br;
	string s1, s2;
	int x1, x2;
	__int128 val;
	bool p=0;
	while(true){
		getline(cin, s);
		if(s=="}"){
			break;
		}
		br=0;
		while(s[br]!='_'){
			br++;
		}
		if(s[br-2]=='m'){
			p=1;
		}
		br++;
		s1="";
		while(s[br]!=','){
			s1.push_back(s[br]);
			br++;
		}
		br++;
		s2="";
		while(s[br]!='"'){
			s2.push_back(s[br]);
			br++;
		}
		while(s[br]<'0' || s[br]>'9'){
			br++;
		}
		if(ind.find(s1)==ind.end()){
			ind[s1]=curr++;
		}
		if(ind.find(s2)==ind.end()){
			ind[s2]=curr++;
		}
		x1=ind[s1];
		x2=ind[s2];
		val=0;
		while(s[br]>='0' && s[br]<='9'){
			val*=10;
			val+=s[br]-'0';
			br++;
		}
		if(p){
			volume.push_back(val);
		}
		else{
			edge.push_back({x1, x2});
			close.push_back(val);
			weight.push_back(-log(val/1e8));
		}
	}
	n=ind.size();
	m=edge.size();
/*	for(int i=0; i<edge.size(); i++){
		cout << edge[i].first << ' ' << edge[i].second << ' '  << weight[i] << '\n';
	}*/
	
	return 0;
}
