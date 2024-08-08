#include <iostream>
#include <list>
using namespace std;

class YoutubeChannel {
private:
    string Name;
    int SubscribersCount;
    list<string> PublishedVideosTitles;
protected:
    string OwnerName;
    int ContentQuality;
public:
    YoutubeChannel(string name, string ownerName) {
        Name = name;
        OwnerName = ownerName;
        SubscribersCount = 0;
        ContentQuality = 0;
    }

    void GetInfo() {
        cout << "Name: " << Name << endl;
        cout << "Owner Name: " << OwnerName << endl;
        cout << "Subscriber's Count: " << SubscribersCount << endl;
        cout << "Videos: " << endl;
        for(string videoTitle: PublishedVideosTitles) {
            cout << videoTitle <<endl;
        }

    }
    void Subscribe() {
        SubscribersCount++;
    }
    void Unsubscribe() {
        if (SubscribersCount > 0) {
            SubscribersCount--;

        }
    }
    void PublishVideo(string title) {
        PublishedVideosTitles.push_back(title);
    }
    void CheckAnalytics() {
        if(ContentQuality < 5) 
            cout << Name << " has bad quality content." << endl;
        else
            cout << Name << " has a good quality content." << endl;
    }
};

class CookingYoutubeChannel:public YoutubeChannel {
public:
    CookingYoutubeChannel(string name, string ownerName):YoutubeChannel(name, ownerName) {

    }

    void Practice() {
        cout << OwnerName << " is practicing coding, learning new languages, experimenting with apps..." 
             << endl;
        ContentQuality++;
    }
};

class SingersYoutubeChannel:public YoutubeChannel {
public:
    SingersYoutubeChannel(string name, string ownerName):YoutubeChannel(name, ownerName) {

    }

    void Practice() {
        cout << OwnerName << " is singing, learning new songs and dancing..." << endl;
        ContentQuality++;
    }
};

int main() 
{
    CookingYoutubeChannel ytChannel("Lynn's Laptop", "Lynn");
    ytChannel.Practice();

    SingersYoutubeChannel singersYtChannel("NyxSings", "Nyx");
    singersYtChannel.Practice();
    singersYtChannel.Practice();
    singersYtChannel.Practice();
    singersYtChannel.Practice();
    singersYtChannel.Practice();

    YoutubeChannel * yt1 = &ytChannel;
    YoutubeChannel * yt2 = &singersYtChannel;

    yt1->CheckAnalytics();
    yt2->CheckAnalytics();

    return 0;
}